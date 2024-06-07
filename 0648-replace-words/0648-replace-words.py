class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root_dict = {root: True for root in dictionary}
        words = sentence.split()

        def find_root(word):
            for i in range(1, len(word)):
                if word[:i] in root_dict:
                    return word[:i]
            return word

        modified_words = [find_root(word) for word in words]
        return " ".join(modified_words)
