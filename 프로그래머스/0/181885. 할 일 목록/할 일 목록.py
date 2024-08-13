def solution(todo_list, finished):
    result = []
    for t, f in zip(todo_list, finished):
        if not f:
            result.append(t)

    return result