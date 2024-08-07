import urllib.request
import json, math

# 해당 사이트에서 발급 받은 키
service_key = '9d0c98f3102bb6ff6211bf2ecdee5831'

def getDataFromWeb(url):
    # url 정보를 이용하여 해당 웹 사이트에서 json 데이터를 읽어 옵니다.
    req = urllib.request.Request(url) # 요청 객체
    try:
        response = urllib.request.urlopen(req) # 응답 객체
        # http 응답 코드가 성공이면 200을 반환합니다.
        if response.getcode() == 200:
            # 바이트 타입을 문자열로 변환하여 반환합니다.
            return response.read().decode('UTF-8')

    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
# end def getDataFromWeb

def movieExtractor(pageNumber, pageSize, thisYear):
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'

    parameter = '?key=' + service_key
    parameter += '&curPage=' + str(pageNumber)
    parameter += '&itemPerPage=' + str(pageSize)

    url = end_point + parameter
    print(url)

    jsonData = getDataFromWeb(url)

    if jsonData == None :
        return None
    else:
        try:
            return json.loads(jsonData)
        except Exception as err :
            print('JSON 데이터에 문제가 있습니다.')
            print(err)
            return None
        # end try
    # end if
# end def movieExtractor

def makeMovieTable(movieData):
    pass
# end def makeMovieTable

print('크롤링 중입니다. 잠시만 기다려 주세요.')

startYear, endYear = 2024, 2025
pageSize = 100 # 최대 100개까지 가능함

for thisYear in range(startYear, endYear):
    print('%s년도 크롤링중입니다.' % thisYear)
    pageNumber = 1

    while True:
        movieData = movieExtractor(pageNumber, pageSize, thisYear)
        print(movieData)

        try:
            totCnt = movieData['movieListResult']['totCnt']

        except Exception as err:
            # 이번 페이지에 존재하지 않으면 다음 페이지로 넘어 가세요.
            pageNumber += 1
            continue

        if pageNumber == 1:  # 1페이지일 때만 전체 개수를 출력합니다.
            print('데이터 총 개수 : ' + str(totCnt))

        if totCnt == 0:  # 0이면 더이상 존재하지 않는 것으로 간주합니다.
            break

        totalPage = math.ceil(totCnt/pageSize)
        print('진행 중인 페이지 : ' + str(pageNumber) + '/' + str(totalPage))

        # if pageNumber == totalPage:
        if pageNumber == 3:
            break # 마지막 페이지에 도달하면 끝내기

        pageNumber += 1 # 다음 페이지로 이동하기
    # end while
# end for

print('크롤링이 끝났습니다.')










