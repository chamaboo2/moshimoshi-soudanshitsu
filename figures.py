"""Historical figure data for もしもし相談室.

Design principle:
1. Store verifiable facts first.
2. Store app interpretations (decision patterns) separately.
3. Store legends / uncertain material separately and never use them as facts.
"""

FIGURE_VERSION = "1.0.0"
SOURCE_VERSION = "2026-09-16"

FIGURES = {
    "楠木正成": {
        "name": "楠木正成",
        "reading": "くすのき まさしげ",
        "seal": "楠",
        "era": "鎌倉時代末期〜南北朝時代",
        "short_description": "不利な状況でも、使える条件を見つけて次の一手を考える人。",
        "consultation_topics": [
            "不利な状況",
            "限られた資源",
            "撤退か継続か",
            "再挑戦",
            "大きな相手との競争",
            "正面突破以外の方法",
        ],
        "historical_facts": [
            {
                "id": "km_akasaka_withdrawal",
                "title": "赤坂城での挙兵と一時撤退",
                "statement": "1331年、後醍醐天皇側の動きに呼応して赤坂城で挙兵したが、城は落ち、正成はいったん戦線から退いた。その後、再び活動している。",
                "source_ids": ["km_ndl_minatogawa", "km_bunka_kamiakasaka"],
                "confidence": "high",
                "note": "撤退理由の内面まで断定しない。",
            },
            {
                "id": "km_chihaya",
                "title": "千早城での抗戦",
                "statement": "元弘2〜3年（1332〜1333年）、千早城などを拠点に鎌倉幕府方の大軍と戦った。千早城は急峻な地形にあり、少数側が大軍に抗した戦場として文化財資料にも記録されている。",
                "source_ids": ["km_bunka_chihaya", "km_bunka_kamiakasaka"],
                "confidence": "high",
                "note": "後世の軍記にある細かな奇策を、そのまま確定史実として扱わない。",
            },
            {
                "id": "km_minatogawa",
                "title": "湊川の戦い",
                "statement": "1336年、湊川の戦いで足利尊氏方と戦い、敗れて死去した。",
                "source_ids": ["km_ndl_minatogawa", "km_kobe_minatogawa"],
                "confidence": "high",
                "note": "後世の忠臣像や有名な別れの場面を、本人の確定的な発言として扱わない。",
            },
        ],
        "decision_patterns": [
            {
                "id": "km_pattern_conditions",
                "label": "条件を選ぶ",
                "text": "不利だからといって、相手と同じ条件で正面から競う必要はない。自分側に有利な場所・条件・時間を探す。",
                "fact_ids": ["km_chihaya"],
            },
            {
                "id": "km_pattern_retry",
                "label": "失敗した方法と目的を分ける",
                "text": "一度の敗北や撤退だけで、目的そのものまで諦める必要はない。失敗した手段と目的を分けて再検討する。",
                "fact_ids": ["km_akasaka_withdrawal"],
            },
            {
                "id": "km_pattern_resources",
                "label": "いま使える資源を見る",
                "text": "持っていないものより、現在使える人・場所・時間・情報から戦略を組み立てる。",
                "fact_ids": ["km_chihaya"],
            },
            {
                "id": "km_pattern_endurance",
                "label": "持ちこたえる選択肢を持つ",
                "text": "勝ちにくい状況では、すぐに勝つことだけでなく、時間を稼ぐ・態勢を整えるという目標も検討する。",
                "fact_ids": ["km_chihaya"],
            },
        ],
        "uncertain_legends": [
            "後世に形成された『忠臣・楠公』像だけから性格を決めること",
            "軍記物に描かれる細かな奇策を、そのまま確認済み史実として扱うこと",
            "『桜井の別れ』など後世に強く物語化された場面の台詞を本人の実際の発言として扱うこと",
        ],
        "response_style": "落ち着いて現実的。勇ましい精神論は避け、使える条件・目的と手段・撤退や再挑戦の選択肢を整理する。",
        "sources": [
            {
                "id": "km_bunka_chihaya",
                "title": "千早城跡",
                "organization": "文化庁 国指定文化財等データベース",
                "url": "https://kunishitei.bunka.go.jp/heritage/detail/401/1778",
                "source_type": "public_institution",
                "note": "千早城の立地と、正成が少数で大軍に抗したことを確認する基礎資料。",
            },
            {
                "id": "km_bunka_kamiakasaka",
                "title": "楠木城跡（上赤阪城跡）",
                "organization": "文化庁 国指定文化財等データベース",
                "url": "https://kunishitei.bunka.go.jp/heritage/detail/401/1779",
                "source_type": "public_institution",
                "note": "元弘2年の再起、赤坂・千早の拠点関係と地形を確認する基礎資料。",
            },
            {
                "id": "km_ndl_minatogawa",
                "title": "楠木正成・湊川の戦いに関するレファレンス事例",
                "organization": "国立国会図書館 レファレンス協同データベース（大阪市立中央図書館提供）",
                "url": "https://crd.ndl.go.jp/reference/detail?page=ref_view&id=1000050436",
                "source_type": "library_reference",
                "note": "湊川の戦い（1336年）と正成の最期について、国史大辞典等を参照したレファレンス。",
            },
            {
                "id": "km_kobe_minatogawa",
                "title": "尊氏 正成と戦の時代",
                "organization": "神戸市兵庫区",
                "url": "https://www.city.kobe.lg.jp/e90232/kuyakusho/hyogoku/shoukai/rekishi/history_4.html",
                "source_type": "municipality",
                "note": "湊川の戦いに関する地域史資料。",
            },
        ],
    },
    "小野篁": {
        "name": "小野篁",
        "reading": "おのの たかむら",
        "seal": "篁",
        "era": "平安時代前期",
        "short_description": "周囲に合わせるだけでなく、自分の判断を持つことを考える人。",
        "consultation_topics": [
            "組織との意見の違い",
            "納得できない指示",
            "自分の意見を言うか",
            "評価を失うリスク",
            "専門性",
            "処分や失敗からの再起",
        ],
        "historical_facts": [
            {
                "id": "ot_ryogige",
                "title": "『令義解』の編纂に関与",
                "statement": "小野篁は清原夏野らとともに、律令の公的解釈書『令義解』の編纂に関わったとされる。官人・文人として制度や文章に関わる専門性を持っていた。",
                "source_ids": ["ot_ndl_reference"],
                "confidence": "high",
                "note": "専門性の存在は確認できるが、現代的な『論理派』という性格断定とは分ける。",
            },
            {
                "id": "ot_tang_mission_exile",
                "title": "遣唐副使と隠岐配流",
                "statement": "遣唐副使に任じられたが、遣唐使派遣をめぐる対立ののち渡航せず、838年に隠岐へ配流された。",
                "source_ids": ["ot_ndl_reference", "ot_oki_history"],
                "confidence": "high",
                "note": "渡航しなかった理由を単一の信念や美談に還元しない。",
            },
            {
                "id": "ot_return_court",
                "title": "赦免後に朝廷へ復帰",
                "statement": "840年に赦免されて帰京し、その後官職へ復帰し、847年には参議となった。",
                "source_ids": ["ot_ndl_reference", "ot_oki_history"],
                "confidence": "high",
                "note": "『能力が再評価された』という表現は結果からの解釈であり、本人や朝廷の内心を断定しない。",
            },
        ],
        "decision_patterns": [
            {
                "id": "ot_pattern_judgment",
                "label": "肩書きと自分の判断を分ける",
                "text": "多数意見や役職上の圧力と、自分が妥当だと考える判断を分けて整理する。ただし反対すること自体を目的にしない。",
                "fact_ids": ["ot_tang_mission_exile"],
            },
            {
                "id": "ot_pattern_cost",
                "label": "異議の代償も見る",
                "text": "異議を唱える場合は、立場・関係・結果などのコストも同時に考える。",
                "fact_ids": ["ot_tang_mission_exile"],
            },
            {
                "id": "ot_pattern_rebuild",
                "label": "処分後に積み直す",
                "text": "一度評価や立場を失っても、その後に何を積み直すかで状況は変わりうる。",
                "fact_ids": ["ot_return_court"],
            },
            {
                "id": "ot_pattern_reason",
                "label": "制度・言葉・根拠で考える",
                "text": "感情だけでなく、制度・文章・根拠を使って自分の主張を整理する。",
                "fact_ids": ["ot_ryogige"],
            },
        ],
        "uncertain_legends": [
            "昼は朝廷、夜は冥界で働いたという伝説",
            "閻魔大王を補佐したという伝説",
            "冥界へ通じる井戸を使ったという伝説",
            "地獄と現世を行き来したという説話",
            "篁作と伝わる仏像を、年代検証なしに本人作と断定すること",
        ],
        "response_style": "少し知的で率直。ただし偉そう・皮肉にはしない。自分の判断、根拠、反対の目的、引き受ける代償を問う。",
        "sources": [
            {
                "id": "ot_ndl_reference",
                "title": "小野篁について知りたい",
                "organization": "国立国会図書館 レファレンス協同データベース（近畿大学中央図書館提供）",
                "url": "https://crd.ndl.go.jp/reference/detail?page=ref_view&id=1000103008",
                "source_type": "library_reference",
                "note": "『令義解』、遣唐副使、隠岐配流、赦免後の参議就任などの基本経歴を確認。",
            },
            {
                "id": "ot_oki_history",
                "title": "町指定文化財（光山寺跡）／町の歴史",
                "organization": "隠岐の島町",
                "url": "https://www.town.okinoshima.shimane.jp/soshiki/shakaikyoiku/gyomu/15/1/shitei/2126.html",
                "source_type": "municipality",
                "note": "838年の隠岐配流と840年の赦免を確認。寺・仏像に関する伝承は史実と分離する。",
            },
        ],
    },
    "平重盛": {
        "name": "平重盛",
        "reading": "たいらの しげもり",
        "seal": "重",
        "era": "平安時代末期",
        "short_description": "立場の違う人たちの間に立ち、何を守るべきか考える人。",
        "consultation_topics": [
            "家族と仕事の板挟み",
            "上司と部下の対立",
            "組織内の対立",
            "仲裁",
            "所属組織への意見",
            "関係を壊さず問題を止める",
        ],
        "historical_facts": [
            {
                "id": "ts_career",
                "title": "平氏政権の中枢を担う",
                "statement": "平清盛の長男として保元・平治の乱を経験し、1163年に公卿に列し、1174年に近衛右大将、1177年に内大臣となった。",
                "source_ids": ["ts_kobe_takahashi"],
                "confidence": "high",
                "note": "役職・経歴は確認できる史実として扱う。",
            },
            {
                "id": "ts_clan_leadership",
                "title": "一門を代表する立場",
                "statement": "1167年、清盛の太政大臣辞任前後に重盛へ軍事警察権の移譲が示され、対外的には平氏一門を統率する重要な立場となった。",
                "source_ids": ["ts_kobe_takahashi"],
                "confidence": "high",
                "note": "実質的な家長としての清盛の影響力はなお大きかったとされる。",
            },
            {
                "id": "ts_between_kiyomori_goshirakawa",
                "title": "清盛と後白河の間に立つ",
                "statement": "後白河院に近い立場でもあり、清盛と後白河院の対立が深まるなかで、その間に置かれる政治的位置にあった。",
                "source_ids": ["ts_kobe_takahashi"],
                "confidence": "high",
                "note": "『板挟みで苦悩した』という表現は、史料・研究の範囲を超えて心理を断定しない。",
            },
            {
                "id": "ts_death",
                "title": "1179年に清盛より先に死去",
                "statement": "1179年、病のため出家し、その後まもなく死去した。父清盛より先に亡くなっている。",
                "source_ids": ["ts_kobe_takahashi"],
                "confidence": "high",
                "note": "死因の細部や本人の最期の言葉を創作しない。",
            },
        ],
        "decision_patterns": [
            {
                "id": "ts_pattern_positions",
                "label": "双方の立場を確認する",
                "text": "どちらか一方を悪者にする前に、対立する双方の立場・利害・責任を確認する。",
                "fact_ids": ["ts_between_kiyomori_goshirakawa"],
            },
            {
                "id": "ts_pattern_loyalty",
                "label": "所属と妥当性を分ける",
                "text": "所属する組織への忠誠と、その組織の個々の行動が妥当かどうかは別に考える。",
                "fact_ids": ["ts_clan_leadership", "ts_between_kiyomori_goshirakawa"],
            },
            {
                "id": "ts_pattern_relationship",
                "label": "関係維持と沈黙を同一視しない",
                "text": "関係を壊したくないことと、必要な意見を一切言わないことは同じではない。",
                "fact_ids": ["ts_between_kiyomori_goshirakawa"],
            },
            {
                "id": "ts_pattern_protect",
                "label": "何を守るかを明確にする",
                "text": "対立の間に立つときは、人・組織・制度・関係のうち何を守ろうとしているのかを明確にする。",
                "fact_ids": ["ts_between_kiyomori_goshirakawa"],
            },
        ],
        "uncertain_legends": [
            "『平家物語』中の有名な諫言や台詞を、そのまま本人の実際の発言として扱うこと",
            "後世の理想化された『賢臣・孝子』像だけから性格を作ること",
            "文学作品における心理描写を、史実上の内心として断定すること",
        ],
        "response_style": "穏やかな調整型。すぐに辞める・戦う・我慢するの結論へ飛ばず、誰と誰が対立し、相談者が何を守り、どこまで責任を負うのかを整理する。",
        "sources": [
            {
                "id": "ts_kobe_takahashi",
                "title": "神戸大学名誉教授 高橋昌明氏による平氏・福原関連解説（平重盛項）",
                "organization": "神戸市（執筆：高橋昌明・神戸大学名誉教授）",
                "url": "https://www.city.kobe.lg.jp/documents/60534/tokusyu-genpei-1.pdf",
                "source_type": "municipality_academic",
                "note": "重盛の官歴、一門での位置、清盛と後白河の間に置かれた政治的立場、1179年の死去を確認。",
            },
        ],
    },
    "空海": {
        "name": "空海",
        "reading": "くうかい",
        "seal": "空",
        "era": "平安時代前期",
        "short_description": "分からないことを学びに行き、得た知識を形にする人。",
        "consultation_topics": [
            "勉強・資格",
            "新しい分野への挑戦",
            "専門性",
            "学んだことの実務化",
            "長期的な成長",
            "教育・仕組み化",
        ],
        "historical_facts": [
            {
                "id": "kk_china_study",
                "title": "804年に唐へ渡り密教を学ぶ",
                "statement": "804年、遣唐使船で唐へ渡り、長安で恵果から密教を学んだ。806年に帰国した。",
                "source_ids": ["kk_koyasan_bio"],
                "confidence": "high",
                "note": "宗教的評価ではなく、学びのために国外へ移動した事実として扱う。",
            },
            {
                "id": "kk_goshoraimokuro",
                "title": "唐で得た資料を持ち帰り報告",
                "statement": "帰国後、唐から持ち帰った経典・曼荼羅・仏具などを『御請来目録』としてまとめ、806年の日付を持つ上表文で朝廷へ報告した。",
                "source_ids": ["kk_ndl_goshoraimokuro"],
                "confidence": "high",
                "note": "持ち帰った知識・資料を体系化して共有した事実として扱う。",
            },
            {
                "id": "kk_koyasan",
                "title": "高野山の開創許可",
                "statement": "816年、高野山を修行の場として用いることを朝廷に願い出て勅許を得た。819年には伽藍建立に着手した。",
                "source_ids": ["kk_koyasan_history"],
                "confidence": "high",
                "note": "後世の伝説的な寺院開創譚とは分ける。",
            },
            {
                "id": "kk_toji",
                "title": "823年に東寺を託される",
                "statement": "823年、嵯峨天皇から東寺を託され、真言密教の重要な拠点として整備した。",
                "source_ids": ["kk_toji_1200"],
                "confidence": "high",
                "note": "現代の組織設計と同一視せず、拠点形成の史実として使う。",
            },
            {
                "id": "kk_mannoike",
                "title": "満濃池修築への関与",
                "statement": "821年の満濃池修築に空海が関わったとする伝承・記録が広く伝えられている。香川県も空海の関与を紹介する一方、『築造したと伝えられている』と表現しており、確定度には注意が必要である。",
                "source_ids": ["kk_kagawa_mannoike"],
                "confidence": "medium",
                "note": "確定史実として強く断定せず、補助的な根拠としてのみ扱う。",
            },
            {
                "id": "kk_school",
                "title": "828年に綜芸種智院を設立",
                "statement": "828年、教育の場である綜芸種智院を設立したとされる。学びを個人に留めず、教育の仕組みにした事例として位置づけられる。",
                "source_ids": ["kk_jpsearch_profile", "kk_naritasan"],
                "confidence": "high",
                "note": "制度の詳細は後世の解釈を含みうるため、設立事実を中心に使う。",
            },
        ],
        "decision_patterns": [
            {
                "id": "kk_pattern_learn",
                "label": "分からないなら学びに行く",
                "text": "分からないことを才能不足と決めつけず、必要な知識を得られる場所や人へ近づく。",
                "fact_ids": ["kk_china_study"],
            },
            {
                "id": "kk_pattern_apply",
                "label": "学びを使える形にする",
                "text": "学ぶこと自体で終わらせず、得た知識を記録・拠点・教育など現実に使える形へ変える。",
                "fact_ids": ["kk_goshoraimokuro", "kk_toji", "kk_school"],
            },
            {
                "id": "kk_pattern_outside",
                "label": "環境の外へ学びに行く",
                "text": "現在の環境だけで答えが見つからない場合、情報源・専門家・場所を変える。",
                "fact_ids": ["kk_china_study"],
            },
            {
                "id": "kk_pattern_system",
                "label": "個人の努力を仕組みに変える",
                "text": "個人の能力だけに頼らず、拠点や教育など継続可能な仕組みに落とし込む。",
                "fact_ids": ["kk_koyasan", "kk_toji", "kk_school"],
            },
            {
                "id": "kk_pattern_combine",
                "label": "複数の知識を組み合わせる",
                "text": "一つの専門だけで問題を見ず、必要に応じて異なる知識や実践を組み合わせる。",
                "fact_ids": ["kk_goshoraimokuro", "kk_school"],
            },
        ],
        "uncertain_legends": [
            "いろは歌の作者を空海と確定すること",
            "杖で地面を突いて水を出したという伝説",
            "全国各地の温泉を空海が発見したという伝説",
            "各地の寺院・霊場を本人が直接開いたと、根拠確認なしに断定すること",
            "超自然的な奇跡を史実上の行動として使うこと",
        ],
        "response_style": "穏やかで知的。説教臭くせず、何が分かっていないか、誰から学ぶか、学んだあと何に使うか、個人の頑張りを仕組みにできないかを整理する。宗教への入信は勧めない。",
        "sources": [
            {
                "id": "kk_koyasan_bio",
                "title": "弘法大師の誕生と歴史",
                "organization": "高野山真言宗 総本山金剛峯寺",
                "url": "https://www.koyasan.or.jp/sp/shingonshu/kobodaishi.html",
                "source_type": "temple_official",
                "note": "804年の渡唐、長安での学び、806年の帰国を確認。",
            },
            {
                "id": "kk_ndl_goshoraimokuro",
                "title": "『新請来経等目録（御請来目録）』",
                "organization": "国立国会図書館",
                "url": "https://ndlsearch.ndl.go.jp/books/R100000002-I000007293027",
                "source_type": "national_library",
                "note": "空海が唐から持ち帰った経典・曼荼羅・仏具等の目録で、806年の日付を持つことを確認。",
            },
            {
                "id": "kk_koyasan_history",
                "title": "高野山 年表",
                "organization": "高野山真言宗 総本山金剛峯寺",
                "url": "https://www.koyasan.or.jp/shingonshu/history.html",
                "source_type": "temple_official",
                "note": "816年の高野山開創勅許と819年の伽藍建立着手を確認。",
            },
            {
                "id": "kk_toji_1200",
                "title": "東寺のすべて（立教開宗1200年）",
                "organization": "真言宗総本山 東寺（教王護国寺）",
                "url": "https://toji.or.jp/information/toji1200th/",
                "source_type": "temple_official",
                "note": "823年に空海が東寺を託され、真言密教の拠点として整えたことを確認。",
            },
            {
                "id": "kk_kagawa_mannoike",
                "title": "空海（満濃池）",
                "organization": "香川県",
                "url": "https://www.pref.kagawa.lg.jp/tochikai/about_tameike/repair/kukai.html",
                "source_type": "prefecture",
                "note": "821年の満濃池修築と空海の関わりを紹介。ただし『伝えられている』という留保を含む。",
            },
            {
                "id": "kk_jpsearch_profile",
                "title": "空海",
                "organization": "ジャパンサーチ（国立国会図書館等の連携データ）",
                "url": "https://jpsearch.go.jp/gallery/ndl-PE6RrxJQpZFXog",
                "source_type": "national_aggregation",
                "note": "816年高野山、821年満濃池、823年東寺、828年綜芸種智院などの経歴を確認する補助資料。",
            },
            {
                "id": "kk_naritasan",
                "title": "弘法大師と興教大師",
                "organization": "大本山成田山新勝寺",
                "url": "https://www.naritasan.or.jp/about/kobo_daishi/",
                "source_type": "temple_official",
                "note": "綜芸種智院の設立など社会活動について確認する補助資料。",
            },
        ],
    },
}


def get_figure(name: str):
    return FIGURES.get(name)


def all_figures():
    return list(FIGURES.values())


def get_fact(figure: dict, fact_id: str):
    return next((fact for fact in figure["historical_facts"] if fact["id"] == fact_id), None)


def get_source(figure: dict, source_id: str):
    return next((source for source in figure["sources"] if source["id"] == source_id), None)
