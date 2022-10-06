# shtelo
> 슈텔로 봇 모델 Python 라이브러리

[슈텔로 봇 프로토콜](https://docs.google.com/document/d/1WpX_88odWCw608wwQtqgb1ohyUa15pmGgr5R2ED10WY/edit?usp=sharing)과
[슈텔로 경제 모델](http://wiki.shtelo.org/index.php/%EC%8A%88%ED%85%94%EB%A1%9C_%EA%B2%BD%EC%A0%9C_%EB%AA%A8%EB%8D%B8)을
파이썬으로 구현하는 라이브러리이다.

## 데이터베이스

이 라이브러리는 특정한 구조의 데이터베이스를 필요로 한다.
어떤 데이터베이스는 적어도 다음과 같은 구조의 테이블을 포함하고 있어야 한다.

```mysql
CREATE TABLE total_value (
    code VARCHAR(5) PRIMARY KEY,
    value DOUBLE
);
```