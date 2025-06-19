
import os
import argparse
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.initializers import glorot_uniform

# Custom sequence encoder/decoder
class IdentityEncoder:
    def __init__(self, seq_len, channel_map):
        self.seq_len = seq_len
        self.n_channels = len(channel_map)
        self.encode_map = channel_map
        self.decode_map = {ix: nt for nt, ix in self.encode_map.items()}

    def encode(self, seq):
        encoding = np.zeros((self.seq_len, self.n_channels))
        for i in range(len(seq)):
            if seq[i] in self.encode_map:
                channel_ix = self.encode_map[seq[i]]
                encoding[i, channel_ix] = 1.
        return encoding

    def decode(self, encoding):
        seq = ''
        for pos in range(encoding.shape[0]):
            argmax_nt = np.argmax(encoding[pos, :])
            seq += self.decode_map[argmax_nt]
        return seq

def generate_5utr(target_mrl, predictor_path, generator_path, n=64, seq_len=50):
    # Load predictor
    predictor = load_model(
        predictor_path,
        custom_objects={
            'GlorotUniform': glorot_uniform(),
        },
        compile=False
    )

    # Load generator
    from genesis.generator import st_sampled_softmax, st_hardmax_softmax
    generator = load_model(
        generator_path,
        custom_objects={
            'st_sampled_softmax': st_sampled_softmax,
            'st_hardmax_softmax': st_hardmax_softmax,
        }
    )

    batch_size = 64
    sequence_class = np.array([0] * n).reshape(-1, 1)
    noise_1 = np.random.uniform(-1, 1, (n, 100))
    noise_2 = np.random.uniform(-1, 1, (n, 100))
    mrl_target = np.full((n,), target_mrl)

    pred_outputs = generator.predict([sequence_class, noise_1, noise_2, mrl_target], batch_size=batch_size)
    sampled_pwm = pred_outputs[6]
    generated_onehot = sampled_pwm[:, 0, :, :, 0]

    encoder = IdentityEncoder(seq_len, {'A': 0, 'C': 1, 'G': 2, 'T': 3})
    generated_sequences = [encoder.decode(generated_onehot[i]) for i in range(n)]
    encoded_seqs = np.array([encoder.encode(seq) for seq in generated_sequences])
    predicted_mrl = predictor.predict(encoded_seqs).flatten()

    results = list(zip(generated_sequences, predicted_mrl))
    results = sorted(results, key=lambda x: abs(x[1] - target_mrl))
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 5'UTR sequences sorted by predicted MRL closeness to target.")
    parser.add_argument('--mrl', type=float, required=True, help="Target MRL value (e.g., 4.5)")
    parser.add_argument('--predictor', type=str, required=True, help="Path to the predictor .h5 model")
    parser.add_argument('--generator', type=str, required=True, help="Path to the generator .h5 model")

    args = parser.parse_args()

    results = generate_5utr(args.mrl, predictor_path=args.predictor, generator_path=args.generator)
    print(f"Generated 64 5'UTRs targeting MRL={args.mrl}, sorted by closeness:")
    for i, (seq, mrl) in enumerate(results):
        print(f"{i+1}: {seq}    (predicted MRL: {mrl:.2f})")
