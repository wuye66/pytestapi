import pytest
import getapi
import postapi


@pytest.mark.get
def test_get_01():
    a = getapi.webrequest()
    r = a.Interface('https://www.jianshu.com','/shakespeare/notes/26213219/included_collections?','page=1&count=7')

    assert r == 403

@pytest.mark.post
def test_post_01():
    a = postapi.webrequest()
    host = 'https://www.jianshu.com'
    api = '/shakespeare/notes/26213219/included_collections'
    data = '{abc=1}'
    r = a.Interface(host,api,data)
    print(r)

#if __name__ == '__main__':
#    pytest.main()
