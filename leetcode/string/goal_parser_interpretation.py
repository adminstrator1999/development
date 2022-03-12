class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        for i in range(len(command)):
            if command[i] == 'G':
                output += 'G'
            elif command[i:i + 2] == '()':
                output += 'o'
            elif command[i:i + 2] == '(a':
                output += 'al'
        return output

    def interpret_brute_force(self, command: str) -> str:
        output = []
        for i in range(len(command)):
            if command[i] == 'G':
                output.append('G')
            elif command[i:i + 2] == '()':
                output.append('o')
            elif command[i:i + 2] == '(a':
                output.append('al')
        return "".join(output)

    def interpret_easy(self, command: str) -> str:
        output = []
        commands = ["G", "()", "(al)"]
        for i in range(len(command)):
            if command[i] in commands:
                output.append(command[i])
            elif command[i:i + 2] in commands:
                output.append('o')
            elif command[i:i + 4] in commands:
                output.append('al')
        return "".join(output)


command = "(al)G(al)()()G"
solution = Solution()
print(solution.interpret(command))
