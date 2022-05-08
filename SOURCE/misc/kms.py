import hashlib
import random


def separate_delete(sep_string: str, sep="-"):
    if len(sep_string) > 0:
        while sep in sep_string:
            sep_string.replace(sep, "")
        return sep_string
    else:
        return None


def separate_insert(sep_string: str, block_len=6):
    if len(sep_string) > block_len:
        pass
    else:
        return sep_string


class SimpleKMS:
    @staticmethod
    def get_activation(reg_number: str):
        reg_number = separate_delete(reg_number)
        i = 0
        activation = []
        while i < 4:
            current = reg_number[i*6:i*6-1]
            md5hash = hashlib.md5(current.encode()).hexdigest()
            activation.append(md5hash[:5])

        checker = ""
        for i in activation:
            checker = checker + i
        checksum = hashlib.md5(checker.encode()).hexdigest()
        activation.append(checksum[:5])
        return activation




    @staticmethod
    def generate_licenses(value):
        codes = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
            '2', '3', '4', '5', '6', '7', '8', '9')
        n = 1
        licenses = []
        while n <= value:
            reg = ""
            for i in range(6*4):
                reg = reg + codes[random.randint(0, len(codes))]

            licenses.append([reg, SimpleKMS.get_activation(reg)])
            n += 1

        return licenses




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
