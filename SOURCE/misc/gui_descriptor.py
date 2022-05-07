import hashlib


class KMS:

    def __init__(self):
        """
        Initialization object of KMS class
        """
        self.regnumb = ""

    def set_params(self, reg: str):
        """
        Set parameters to find license combination
        :param reg: registration number (string mod to 6, ex. XXXXXX-XXXXXX-...-XXXXXX is N block with 6 symbols each)
        :param owner: string with name of license owner (using only in 2nd generation of licensing)
        """
        self.regnumb = reg

    def get_activation(self, external=None):
        """
        Finding correct combination
        :return: list of N+1 blocks
        """
        block_score = len(self.regnumb) // 6
        activation_blocks = []
        iteration = 1
        while block_score > 0:
            block_start = 6 * iteration - 6
            block_finish = 6 * iteration - 1
            temp_block = self.regnumb[block_start:block_finish]
            block_hash = hashlib.md5(temp_block.encode()).hexdigest()
            activation_blocks.append(block_hash[0:6])

            block_score -= 1
            iteration += 1

        checksum = ""
        for block in activation_blocks:
            checksum = checksum + block

        checksum_hash = hashlib.md5(checksum.encode()).hexdigest()
        activation_blocks.append(checksum_hash[0:6])

        return activation_blocks
