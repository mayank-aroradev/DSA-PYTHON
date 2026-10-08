class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
    # 1. Store the last occurrence index of each character
            last_idx = {char: i for i, char in enumerate(s)}
            
            stack = []
            seen = set()  # Tracks characters currently inside the stack
            
            for i, char in enumerate(s):
                # Skip the character if it is already in our result
                if char in seen:
                    continue
                    
                # Maintain monotonic order:
                # Pop the top character if it's larger than the current character
                # AND it appears again later in the string
                while stack and char < stack[-1] and last_idx[stack[-1]] > i:
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                    
                # Push the current character onto the stack and mark it as seen
                stack.append(char)
                seen.add(char)
                
            # Combine the stack into the final string
            return "".join(stack)
