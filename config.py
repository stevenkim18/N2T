from utils.dotdict import dotdict

cfg = dotdict(
    TISTORY=dotdict(
        ID='11882@naver.com',
        PW='Steven9736!@',
        BLOG_NAME='stevenkim18',
        SECRET_KEY='1f28168a173ecb51fc6452573dcce46f60ee9cb5c980b0116adede48e81892beb7432dda',
        CLIENT_ID='1f28168a173ecb51fc6452573dcce46f',
        REDIRECT_URI='https://stevenkim18.tistory.com',
    ),

    NOTION=dotdict(
        TOKEN_V2='940d3e07ed824269e0de1c8b3a9b882871a0435d096aac480ebc6dee9ded7294ff89ce1c5761f418f78d427cfbb12838bf3eb191102d3cc1f915f60a85ff0ecf347ae0a2f7cc57a0f3c4f7bb9d66',
        TABLE_PAGE_URL='https://www.notion.so/stevenkim18/936b04c5c47449538ca44d7559beee29?v=5430cf5bd87c430d8700cf70599a6b6e',
        DOWNLOAD_DIR='~/.n2t',
        CODE_BLOCK_THEME='atom-one-dark',

        COLUMN=dotdict(
            TITLE='제목',
            CATEGORY='카테고리',
            TAG='태그',
            STATUS='상태',
            URL='링크'
        ),

        POST=dotdict(
            UPLOAD_VALUE='발행 요청',
            MODIFY_VALUE='수정 요청',
            COMPLETE_VALUE='발행 완료',
        ),
    ),

    MAIL=dotdict(
        ID='',
        KEY='',
    )
)
