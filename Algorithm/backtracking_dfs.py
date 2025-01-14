def backtracking_dfs(words, path, used):
    # 해답 조건을 검사하여 조건을 만족하면 현재 경로를 반환합니다.
    if is_solution(path):
        return path

    # 단어 목록을 순회하며 탐색을 수행합니다.
    for i, word in enumerate(words):
        # 단어가 아직 사용되지 않았고, 경로에 유효하다면
        if not used[i] and is_valid(path, word):
            path.append(word) # 경로에 단어를 추가합니다.
            used[i] = True    # 해당 단어를 사용했다고 표시합니다.

            # 재귀 호출을 통해 더 깊게 탐색합니다.
            result = backtracking_dfs(words, path, used)
            if result:
                return result

            # 백트래킹 단계: 단어를 경로에서 제거하고, 사용하지 않았다고 표시합니다.
            path.pop()
            used[i] = False

    # 해답을 찾지 못한 경우 None을 반환합니다.
    return None

def is_solution(path):
    # 예시로, 경로의 길이가 5이면 해답으로 간주합니다.
    return len(path) == 5

def is_valid(path, word):
    # 경로가 비어있으면 어떤 단어라도 유효합니다.
    if not path: return True

    # 마지막 단어의 끝 문자와 새 단어의 시작 문자가 같으면 유효합니다.
    return path[-1][-1] == word[0]

words = ["grape", "tiger", "apple", "egg", "elephant"] # 끝말잇기 게임에 사용할 단어 목록
path = [] # 끝말잇기 경로를 저장할 리스트
used = [False] * len(words) # 각 단어의 사용 여부를 저장할 리스트
result = backtracking_dfs(words, path, used) # 백트래킹을 사용한 깊이 우선 탐색을 호출
print("끝말잇기 경로:", result) # 결과 출력