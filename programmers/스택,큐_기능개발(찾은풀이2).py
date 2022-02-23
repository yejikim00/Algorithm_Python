def solution(progresses, speeds):
    # 남은 작업 일수 리스트에 담기
    cnt_lst = []
    for i in range(len(progresses)):
        # 진도율 100%에서 현재 진행된 완료율을 빼줌
        tmp = (100 - progresses[i])
        if (tmp % speeds[i]):
            # 하루 개발 속도로 나누기(올림)
            cnt = tmp // speeds[i] + 1
            cnt_lst.append(cnt)
        else:
            cnt = tmp // speeds[i]
            cnt_lst.append(cnt)

    # 배포마다 몇 개의 기능이 배포되는지 확인
    start = 0   # 작업일 수를 비교하기 위한 기준이 되는 인덱스
    answer = []
    for idx in range(len(cnt_lst)):
        if cnt_lst[start] < cnt_lst[idx]:
            # 기준값보다 그 다음값이 큰 경우에 기능의 개수를 세고
            answer.append(idx-start)
            # 기준값 인덱스 업데이트
            start = idx
    answer.append(len(cnt_lst) - start)
    return answer



progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))