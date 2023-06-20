# LLM-Fine-Tuning-Platform
# 0. 商品名とキャッチフレーズ
商品名：LLM Fine-Tuning Platform
キャッチフレーズ：「ドメイン特化のカスタムモデルでオープンLLMを次のステージへ」

# 1. 問題点
解決したい課題：カスタマイズしたオープンなLLMモデルを精度を維持し続けながら公開したい。MLOpsへの貢献、計算リソースの提供をした人に対してインセンティブを払いたい。

 前提：
・昨今の生成AI界隈ですが、LLM、画像系、音声系と複数のジャンルがあります。画像系と音声系はオープンソースがブームを牽引しています。LLMは現状クローズドソースであるOpenAIとGoogleがブームを牽引しています。
・そんな中、LLMもオープンソース化へ取り組む企業があり、サイバーエージェントやrinnaから日本語コーパスで学習させたモデルが公開されています。web3的にはビッグテックが提供するクローズドモデル以外の選択肢が生まれるのは良いことだと思います。
・さて、LLMですが現実社会に実装していく段になると「フリートーク」の性能は意外と要求されないのではないかと考えています。汎用的で巨大なモデルではなく、特定用途において精度の高い回答を返す小さなモデルを複数使い分けたり組み合わせて、アプリに組み込んでいく使い方がニーズとして高いのではないかと考えます。
・オープンソース化が先行しているStable DiffusionやRVFの進化の仕方を参考にすると、事前学習済みモデルをベースにPEFT(Parameter-Efficient Fine-Tuning)用の追加学習モデルを組み合わせて使うのが主流になるのではないかと仮説を立てました。

・ここで問題なのですが、基本的に機械学習モデルの精度はデプロイ直後が最高であり、その後、学習時に想定されてなかった入力データが増えるに従ってどんどん推論の精度が落ちていきます。これを継続的にデータを見ながら再学習やリモデリングし、精度を維持するMLOpsと言われるプロセスが実運用のフェーズでは重要です。
OpenAIやGoogleは自社サービスを使用したユーザからの全てのフィードバックデータを保持していますので、当然ほぼほぼ自動で精度維持のプロセスが回っていると予想されます。
ところが、オープンソース化されたモデルの場合、特に企業が提供する事前学習済みモデルではなくニッチな用途に合わせてほぼ個人が作成した追加学習モデルの場合、これをメンテし続けて公開し続けるのはボランティアでは開発者への負担が大きすぎます。
また、追加学習モデルを作成する時のマシンスペックもそれなりのものが要求されるため、カスタムモデルのアイデアがあって新規参入したいと考える人達へのハードウェア的なハードルが参入障壁となってしまう可能性もあります。

そんな訳なのでこの課題を解決します。解決するとこんな良い事があります
・自立分散化され、多様性に富んだ生成AI基盤が社会インフラとして実現します。ビッグテックにより提供されるAIと補完し合うことで、全ての人が持続的に生成AIの恩恵を受けられる社会の実現を目指します。

# 2. 解決策
ソリューション：
特定用途向けにファインチューニングされたLLMカスタムモデルの生成、メンテ、APIゲートウェイの機能を持った開発プラットフォームを提供します。

本プラットフォームはWeb2.0とweb3のハイブリッドになります。
Web2.0側機能
・ユーザのログイン、認証認可、アカウントとウォレットアドレスの紐付けと管理機能
・各種操作及び機能拡張のWebUI機能
・生成したカスタムモデル、もしくは複数モデルや他のモデルやサービスとの複合させたアプリを、見た目単一のLLMモデルのように振る舞い、外部アプリに対してAPIを提供する機能
・ユーザ側から受け取った情報とブロックチェーンネットワークとの橋渡しをする機能

web3側機能
・推論
・MLOps協力者の貢献度によるスコアリングとインセンティブの支払い
・計算リソース提供者へのインセンティブの支払い

利用イメージとしてはStable Deffusion WebUIと同様の使用感で、オープンソースの事前学習済みモデルを選択し、作成したQLoRAのモデルと合わせてデプロイしてやると専用のChatGPTライクな画面に遷移し、テスト後、品質に満足したならAPIのURLもしくはAPIキーを発行できるイメージ

# 3. 市場規模
TAM：今後、全てのアプリに何らかの形でAIが組み込まれるようになるとさえ言われているので、インターネットユーザーであればほぼ全員アプリ経由で何らかのAIを利用することになるはず。つまり約30億ユーザぐらい
SAM：その中であっても相変わらずChatGPTとBard（PaLM 2）のシェアは強いと予想されるので、オープンソース系のモデルのシェアは3分の1と仮定して10億、ただし、本サービスは当面日本語圏のユーザを対象とするので1億の3分の1で3000万強
SOM：まずは実証実験とインタビューを行わないことには始まらないので最低2桁ユーザを目指す。オープンソース系の事前学習済みモデルであれば種類を問わないのでChatGPTとBard（PaLM 2）以外のユーザであれば全て取り込める可能性がある

# 4. トラクション
※データなし

# 5. ユニークな洞察
インサイト：PEFTのアプローチとしてLoRAを採用し、更にQLoRAで量子化してやると、学習や推論の計算リソースとしてブロックチェーンのノードでも間に合うのではないか
（今後要実証）無理そうならポルカドット経由してgensyn AIとかから計算機リソースを調達

# 6. ビジネスモデル
一般的なパブリックブロックチェーンエコシステム。IEOを前提。トークンのキャピタルゲインとインカムゲインでWeb2.0側のリソース代を賄いたい。
