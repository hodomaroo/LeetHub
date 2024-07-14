import re
def find_n(text):
    # 입력 문자열의 시작에 숫자가 있는지 확인하는 정규표현식
    start_number_pattern = r'^\d+'
    start_number_match = re.match(start_number_pattern, text)
    return start_number_match.group(0) if start_number_match else 1

def find_pattern(text):
    # 패턴 정의: 대문자로 시작하고 소문자로 끝나며, 1보다 큰 숫자가 뒤따를 수 있는 단어
    pattern = r'\b([A-Z][a-z]*)([0-9]*)?'
    
    # 정규표현식 검색
    match = re.search(pattern, text)
    # 매치 결과 반환
    if match:
        start_pos = match.start()
        end_pos = match.end()
        word = match.group(1)
        number = int(match.group(2)) if match.group(2) else 1
        return [end_pos, word, number]
    else:
        return [None, None, None]


class Solution:
    def countOfAtoms(self, f: str) -> str:
        
        
        stack = [Counter()] #[Counter]
        idx = 0
        while idx < len(f):
            if f[idx] == "(":
                stack.append(Counter())
                idx += 1
            elif f[idx] == ")":
                number = int(find_n(f[idx+1:]))
                ss = stack.pop()
                idx += 1 + (len(str(number)) if number > 1 else 0)
                
                for v in ss:
                    stack[-1][v] += ss[v] * number
            else:
                p_idx, word, number = find_pattern(f[idx:])
                idx += p_idx
                stack[-1][word] += number
        
        return "".join(v+(str(stack[-1][v]) if stack[-1][v] > 1 else "") for v in sorted(stack[-1].keys()))

                         
                
                    
                        
                
                
            
        