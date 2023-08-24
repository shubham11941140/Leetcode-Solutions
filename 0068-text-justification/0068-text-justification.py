class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line, line_length = [], [], 0
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                num_spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * num_spaces)
                else:
                    spaces_between_words = num_spaces // (len(line) - 1)
                    extra_spaces = num_spaces % (len(line) - 1)
                    justified_line = line[0]
                    for i in range(1, len(line)):
                        spaces = spaces_between_words + int(i <= extra_spaces)
                        justified_line += ' ' * spaces + line[i]
                    result.append(justified_line)
                
                line, line_length = [word], len(word)
        
        # Left-justify the last line
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result        