from nacl.signing import SigningKey
import os


if __name__ == '__main__':
    if '.multisig_identity' not in os.listdir():
        signing_key = SigningKey.generate()
        with open('.multisig_identity', 'w') as file:
            file.write(signing_key._seed.hex())
    else:
        with open('.multisig_identity', 'r') as file:
            signing_key = SigningKey(bytes.fromhex(file.read()))

    print(
        f"Your publicKey: {signing_key.verify_key._key.hex()}\n"
    )
