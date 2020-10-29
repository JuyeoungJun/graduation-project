# graduation-project
=====================

요약
----------
소비자와 기업 모두가 소비/생산에 대한 결정을 할 때 중요한 factor로 사용되는 것이 소비자의 리뷰이다. 이러한 리뷰의 데이터가 많아지는 만큼 무의미하고 광고성 리뷰 역시 많아지는 추세이며 이에 따라 소비자와 기업 모두 변별력 있고 신뢰할 수 있는 리뷰를 확보하는 것이 중요해졌다. 

본 프로젝트는 리뷰들을 Deep learning 기반의 모델에 학습시키고, 이 모델을 이용하여 리뷰들의 정보량과 신뢰성에 대해 5단계로 나누어진 평점을 부여하도록 한다. 이 평점을 통하여 더 신뢰할 만한 리뷰들만 뽑아내어, 생산자와 소비자 모두가 리뷰기반의 결정 시 도움을 받을 수 있도록 한다.        
서론 
-----------
1. 과제의 필요성
<리뷰의 중요성과 의미가 없는 리뷰>
 2020년 1월 통계청이 발표한 자료에 따르면, 온라인쇼핑 거래 금액은 12조 3,906억원으로 전년동월대비 15.6%증가하였다. 또한 2020년 기준 소매판매액 중 온라인 쇼핑 거래액이 차지하는 비중은 23.2%에 달한다.
 
이와 같이 최근 온라인 시장이 확대됨에 따라 상품을 직접 확인하고, 선별하는 과정을 거치지 않고 상품을 구매하는 경우가 많다. 이에 따라, 상품에 대한 정보를 얻기 위해 상품을 먼저 구매한 다른 구매자들의 리뷰를 보고 상품에 대한 정보를 얻는 경우가 많아지고 있다. 이에 따라 더 많은 리뷰를 확보하기 위해서 포인트, 적립금을 지급해주는 등의 방식으로 구매자들이 리뷰를 남길 수 있도록 독려하고 있다.  예를 들어, 마이리얼트립은 후기를 작성한 고객에게 쿠폰을 제공하는 등 리뷰를 독려하는 이벤트로 홍보를 대체하고 있다. 그 결과 마이리얼트립에 올라온 누적 여행 후기 수는 2019 3월 기준 47만여 건에 달한다. 하지만 리뷰가 증가함에 따라서 그에 따라 상품광고, 적립금의 받기 위한 리뷰 등 의미가 없는 리뷰도 또한  증가하고 있다. 이러한 의미가 없는 리뷰들은 다음과 같은 다양한 문제를 발생시키고 있다. 

<의미 없는 리뷰의 문제점>
첫 번째로, 객관적인 리뷰를 선별하고 그를 통해서 정보를 얻는 데 까지 오랜 시간이 걸리게 된다. 제품을 구매하는 데 있어서 구매자가 상품들을 리뷰를 읽어보고 그것이 의미가 있는 리뷰인지를 판별하고, 그것을 기반으로 상품 구매를 고려한다. 이 때, 의미가 없는 리뷰가 많으면 그것이 의미가 있는 리뷰인지, 없는 리뷰인지를 판단하는 데에도 시간이 소모되게 된다. 이로 인해, 쓸데 없는 시간 낭비가 발생하게 된다. 

두 번째로, 상품의 점수에 인한 리뷰의 정확성 혼동이 발생한다. 대부분의 의미가 없는 리뷰들은 상품의 평점이 1-5점으로 주어질 때 5점으로 주어지는 경우가 허다하다. 이로 인해서 상품의 평점이 정상보다 높아지게 된다. 이는 리뷰의 정확성에 구매자들이 의문을 품을 가능성을 주게 된다. DMN의 조사에 따르면, 상품의 리뷰가 4.7에서 5점사이에 존재한다면 구매자들은 이 제품에 대한 리뷰가 신뢰성이 없다고 판단한다고 한다.  

 세 번째로, 상품의 광고로써 사용되는 리뷰로 인한 혼동이 발생한다. 최근 많은 기업에서 자신들이 판매하는 상품에 대해서 긍정적인 리뷰를 작성해주는 일명 리뷰 아르바이트를 많이 활용하고 있다. 그 결과, 특정 상품에 대해서 객관적이지 못한 긍정적인 리뷰들이 많이 작성이 되고 있다. 구매자들은 이러한 리뷰가 광고인지 일반 구매자가 작성한 리뷰인지를 구별할 뚜렷한 방법이 없다. 그로 인해서, 상품을 구매하는데 있어서, 상품을 구매하는 과정에서 객관적이지 않는 판단을 발생시킬 가능성이 농후하다.

 네 번째로, 기업이 리뷰를 분석 및 활용할 때  혼동을 초래할 수 있다. 많은 기업들이 상품에 대한 리뷰를 통해서 소비자들의 패턴을 분석하고 이를 활용하고 있다. 이때 의미가 없는 리뷰가 데이터로 존재 한다면 리뷰를 분석의 정확성을 낮추게 된다. 

<과제의 필요성>
 우리는 위에서 언급한 문제들을 해결하기 위해서 리뷰를 분석하여서 그 리뷰가 의미가 있는 리뷰인지 없는 리뷰인지를 판단하고자 한다. 이러한 작업의 필요성은 다음과 같다. 

 첫 번째로, 구매자가 의미가 있는 리뷰와 의미가 없는 리뷰를 분류하는데 낭비되는 시간을 아낄 수 있다. 많은 업무량으로 인해서 바쁜 하루를 보내는 현대인들에게 조금이나마 더 현명한 시간 소비를 할 수 있도록 도움을 줄 수 있다. 

 두 번째로, 리뷰에 대한 신뢰성을 증가시킬 수 있다. 위에서 언급하였듯이 4.7-5점사이의 높은 평점인 상품들은 객관적이지 못하다고 판단할 수 있다. 이로 인해서 정말 좋은 상품에 대한 의구심이 생길 수가 있다. 하지만 의미 없는 리뷰들을 제거하게 된다면 상품에 대한 구매자들의 신뢰성을 확보 할 수 있다. 

 세 번째로, 광고로써 사용되는 리뷰들을 제거함으로써 더 객관적인 소비를 할 수 있다. 상품을 구매하는데 있어서 기업에서 구매자가 더 많은 소비를 할 수 있도록 작성하는 의미가 없는 리뷰들을 제거 함으로써 실제 구매자들의 구매 후기를 통해서 상품을 구매하는 데 있어서 더 현명한 결정을 할 수 있게 된다.

 네 번째로, 기업이 리뷰를 분석하고 활용하는데 도움을 줄 수 있다. 기업이 리뷰를 분석할 때 의미가 없는 리뷰가 분석을 잘 못 된 방향으로 이루어지는 것을 방지 할 수 있기 때문에 기업은 이러한 리뷰를 활용해서 마케팅, 상품 추천 등에 이용함으로써 기업의 이익을 더욱 증가 시킬 수 있다. 

제안 작품 소개
-------------
<작품의 구성>
1. 리뷰 크롤링
- 과제를 진행하는 과정에서 필요한 리뷰 데이터 셋을 웹에서 웹 크롤링을 사용하여서 확보
- Python의 BeautifulSoup 모듈을 활용하여서 정규표현식을 사용해서 html, xml등의 데이터에서 리뷰를 추출

2. 필터링 기준 선정 및 분류
- 필터링 기준 선정 및 선정 기준의 신뢰성 판단
- 판단된 신뢰성에 따라 리뷰의 의미 신뢰도를 분류

3. 분류된 결과를 토대로 한 딥러닝 학습
- Python의 Tensorflow, keras를 이욯하여 딥러닝 모델을 만들고 학습을 진행 

4. 테스트 및 검증
- 실제 리뷰에 적용하여서 리뷰의 신뢰성을 판단
- 적절한 신뢰성을 가지는 도출해 내는지에 대해 검증









