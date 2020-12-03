# def twoSum(nums, target):
#     h = {}
#     for i, num in enumerate(nums):
#         n = target - num
#         if n not in h:
#             h[num] = i
#         else:
#             return [h[n], i]


# print(twoSum([2, 7, 11, 15, 1], 22))
# def lengthOfLongestSubstring(s):
# i = 0
# d = {}
# ans = 0
# for j in range(len(s)):
#     if s[j] not in d or i > d[s[j]]:
#         ans = max(ans, (j-i+1))
#         d[s[j]] = j
#     else:
#         i = d[s[j]]+1
#         ans = max(ans, (j-i+1))
#         j -= 1
# print(ans)
# ---------------------------------------------
#     lastIndex = [-1] * 256
#     res = 0   # Result
#     i = 0

#     for j in range(len(s)):
#         # //
#         i = max(i, lastIndex[ord(s[j])] + 1)
#         res = max(res, j - i + 1)
#         # print(i, res)
#         lastIndex[ord(s[j])] = j
#         # print(ord(s[j]))

#     print(res)


# lengthOfLongestSubstring('keaaw')

# def calPoints(ops):
#     score = []
#     for i in range(len(ops)):
#         if (ops[i] == '+'):
#             scored = score[-1] + score[-2]
#             score.append(int(scored))
#         elif (ops[i] == 'D'):
#             scored = score[-1] * 2
#             score.append(int(scored))
#         elif (ops[i] == 'C'):
#             score.pop(-1)
#         else:
#             score.append(int(ops[i]))

#     return sum(score)


# calPoints(["5", "2", "C", "D", "+"])
# def minimumLengthEncoding(words):
#     ans = []
#     test = []
#     for i in range(len(words)):
#         for word in words:
#             if (word in words[i]) and (word != words[i]):
#                 ans.append(word)
#                 test.append(words[i])

#     s = set(ans)
#     print(ans)
#     print(f'test-{test}')
#     for ele in s:
#         words.remove(ele)
#     s=set(words)
#     s = '#'.join(s)
#     return len(s)+1
            # for i in range(l):
            # if words[i] in words[i+1]:
            #     ans.append(words[i])
            # elif words[i+1] in words[i]:
            #     ans.append(words[i+1])
        # ans=set(ans)
        # for cha in ans:
        #     words.remove(cha)
        # s = set(words)
        # s = '#'.join(s)
        # return len(s)+1

'''
# print(minimumLengthEncoding(["jagmf","ihfbd","wsqmo","lulls","wbkydwk","aisdkal","lgmycw","nyflvm","qzwprd","lwjdqwu","njyhy","gwbzr","tfiwega","jymidsk","ozwai","wenfskk","aagem","mpzwc","izfph","oanix","uvycxu","mafife","rhintr","vodkci","pqldsr","sfcndyy","mzocbxu","rsofltm","cxvyk","sddru","wnrad","gsamzh","wdilpxh","nbgipxl","fhscz","rfuhh","jsezl","uvvmni","teazo","ogaqpcq","pprhmop","xadoc","tctsp","vyaawe","lzycjg","xuqybi","wfcvpe","wqpwnnh","kzgrn","cxnaur","mnqyis","kjjif","mgyou","lauwd","ijfdlv","phgvlq","ncnnbv","kmooheh","iuaeuuj","empbk","ppysu","wnruklt","ubhqva","dgvwa","jipwcy","klqzu","ydewoga","blaeakq","ptqhmi","pdbckk","ybwrfv","waaowot","eqikq","szzarb","ukcbui","nljyw","escvf","uqiwz","gxpwasn","zjkngf","hmnwqx","vjtugg","jowzj","mnythry","tvmla","kuhpqqz","yhbpmfu","ntnghdh","wrvdks","ziqowg","gxqcugq","bnuznys","ejdufyd","xjsafvq","vocdo","tpwxf","cfknk","rruzi","kdlzoio","zzfgj","jxggm","hpkpxc","ygubujf","vmotq","vsbvrny","efkpf","brjcx","kbungq","xmpds","zwpbo","flglia","wtfwdr","enisxz","dgjwnm","jyzdbao","twkdpb","shwvkk","dcqjz","urfwwh","felkw","fzkfcsy","fopdz","ukxqk","wwelyd","fagbz","izeogn","ccviqy","ipcne","gctdevm","oiwilw","bmeesge","ntatsi","cvpvn","xqzuln","wzylc","jgqtid","ntpclv","xxqxup","gsejih","apxhb","ioddg","aehqpju","vpvgou","rmgns","wlyzy","bkrpvv","efmwtz","faumd","iztley","nkncq","ztjhrq","pbmdpo","wcton","anzeb","lkdfdr","bvbfrn","lgnzu","tqjpsx","rslrii","kabxmy","apysgg","mjxrxl","qiqla","qovvr","dsplpyj","rdvopx","rwbftvz","xekky","lnlrudt","lnhlcg","eqoqa","rohrosk","uzauwya","vhvwi","yubqk","xubaz","wbrwf","uxoflle","qwcer","foriiei","hluwmhj","rcjgt","doysixm","hlsddo","girwxxs","mfqlgkw","kixuy","yndqweq","cvqsgs","xjncsl","duhvdx","hojdr","oqrudnz","bukqa","wgepmo","lvfui","ssduod","xqdwmxz","xraamzf","tazruhs","ubrxl","boftae","gwcktng","vgqximi","ntmhdme","qazlcs","udfscu","tnzxhf","vjvzih","tizpp","yhfeue","crgppnx","jtqzn","cavwz","bztnjca","ifxnym","gczxx","iykwjy","vhicst","xymhs","wrerkbf","zefsstd","fqrvvn","iqjkmi","fjbra","elswvf","vwxxoyh","uasowg","glljwp","tuanfxd","znlqyzy","esouttq","tbztdzz","puikopi","pfoezcz","dcuujtm","pfxjxvk","ddjkywv","mbxsntr","gdxqth","bvmfdhd","asknfh","kjcal","slnpo","urgzxg","qwpcia","pbhjbwy","hjjzwm","yuwbrd","inuatc","gjozcrw","rmulq","zjdwiq","wojbj","rfqvc","uksxc","jhqwqy","kvgwdb","vpavuv","zugrk","nzxczv","lhgaz","tepuj","hczcg","nkats","pihhx","lbckst","cyvor","hauib","zoezm","zwntlth","pzocqja","xaixupk","ciepos","bdddt","dmlijl","nlajkv","oukhr","gkyqug","nrbvu","nyomxt","jfmfw","yaovtm","fqweojf","ljtpz","kquur","hywsv","udftjb","dryukdf","lshkv","vshruue","vpmnzhr","jjjugej","ucfjyoo","miszzd","wyzml","txhkei","hxwgb","qinju","munru","ckrgzyj","ptcsk","ivypa","huzrry","oqweczw","zgmxf","kgnwyp","qlimow","thqts","eoiobdq","fuhhva","zcfqe","tcnio","eqekgvp","rnajagk","yvlzve","fbyted","spnzjnv","bmskmx","pwcae","vqusmoi","efema","dtcok","zsdzhol","cyxhe","uuhwo","gpkfns","hhwbvo","onztv","hbsonoj","ftyslrs","thrnrsl","ylgxhsb","qwzyleh","urnyq","zakie","umhlafk","bapwh","bedbkkb","bkywos","zussbw","hclpvdw","ehvnbl","kmafj","rmjsmwk","mdigq","vqpgi","wdtwpoz","tepdac","bfqvmo","gbjpyv","hrbqv","yipgn","jotfx","cltha","uyjefy","hlidyle","tsvzxez","blfisk","tfkdzu","lbvtcm","jracn","lceah","mmjmeo","hulaea","rltdk","olnfq","pbnlio","avxej","lvbmz","yfvdcw","ehrwcq","lobywpx","jicjt","ducziwc","mwgczk","lsjhrbn","xcbjt","yjpiaom","rgapg","waalaqk","julwrha","lztkqv","glseon","xmwthi","jyjudz","bwqjv","ofcmf","hpyioho","qdjfnex","pahbw","riqhsm","chwpgt","yonaug","mqltja","zvmnq","bpnfw","psyuny","wtfqs","nsfxuh","gyoalnb","podan","kewqsb","ntcwq","zbxoh","hdhxw","cumdoem","jnawtu","aiharq","zwkijv","yoqfwx","boeakd","ewlcfj","ytqoith","fptzui","zmtec","bxwsax","igvbkub","akipicx","wphlshw","cxbaml","mtypvc","ffuci","defxt","ilzdra","mgilplo","ebnnlp","tfwzisf","gplmzsx","hgtczd","fvdwu","nwlul","hlcbi","ouzap","pokgaux","holmx","ltnjhx","szmkmv","jjvue","vgnnvj","dahfv","fgvqux","iphia","xksen","rgivzj","ksekxmn","ysofb","hdrxg","sdfgcih","xbamqnw","cltbx","dzazwu","pgjwgw","adxfo","vbsxp","ubskbst","putcju","vdyno","leifyz","xkvusrn","gihjh","akngtvv","aohwa","xxmzwau","xrxpos","ybetqe","swzsutu","xppso","ttxaptm","oqbpxi","jjgqjpa","hkrumc","glmnr","tjdxxs","bggtc","sqacef","aygzdn","pfsyfzj","nkwxlj","oxwiso","rwtnxrm","ajwiewa","asjexsv","cqnlbc","vjhjdp","njlcswl","bvwld","tmuuhyq","uqcdl","vxrcc","wjwzsdd","qzhczlr","wflwtry","apkxg","jyytj","yzwkvp","ryumodv","ekvvp","vgerfbs","ekjrbrd","sdtizv","fubxqh","pxbyogj","wqqhho","mueym","rbszj","dedrcnz","gpbdbo","bslyx","pyfvpoo","faxboxt","bsxmep","ohnrji","hlopws","bbyjeel","ccwnsh","aipida","xfnxiuj","mhaypk","tdruuw","qtwergh","ziucvvy","hchsyv","upixtk","tnkwyq","olqcnwd","fcosa","gdskvc","jigyycq","baxqbs","vwfpq","edofgcl","woznx","urcejk","johvv","knlzlr","nwvvn","axwzhee","dsrki","hqpxzl","mbeedyv","qejjqc","qsnnzvt","gemjhc","hrsgj","uopki","sdwijjr","hisqcd","ytgrqjg","mawufqj","yhjzrsb","rjqtsh","mqrbeh","hnrkbhl","gyirc","lnodoz","girwqhc","molajz","edkvldr","qhyvdi","jovdjoj","tnvwe","yokfhkf","agwtx","jnztnrp","mghhwld","zzafivk","pxrio","nougwx","rxviprt","rymsp","oivoe","hkrxr","wrnoga","parqrw","itxrf","fwhycmu","jwnnm","aczem","yeqcu","fkmuhyz","bsgmquv","dbmeg","cuofam","fqielnr","ewzfkqa","tdculi","vlsgtt","wearqph","ncsqoni","wclgpce","ondjntw","garagd","ufpvjsd","dbeif","kgvrfq","feqpgp","zrapenh","uvdmafv","rtlbc","ihcwec","qmbkp","ljext","rzoutm","vrgmgf","gxdhm","qjqxak","drcntga","jhpbeb","mfamep","pvztosa","ublibo","ckvget","uzxit","ncxqd","wmbsur","vbwbwlj","pxrhx","nxlvwws","qspfdn","qokfy","yhhtjys","tzrsr","jjmiq","yeilg","zqrdcce","txedir","dnszc","dbntq","rooqgiw","knide","uoxyd","iynosd","swjyhud","paehzs","hkzfj","yzxah","dnhzvax","vfehrrv","bwloj","ctkslnl","dyjekdo","yzbmi","ahsjfpt","hjuevb","ycjee","iccvcu","ouhrgbk","xertzjx","dxmdj","nrcoip","pdesb","igkejl","kxgsmk","ktqpp","mfvbenx","ahiypm","egisoo","koqpvz","qqfjrlv","sxqvgjn","xqysb","bvbuc","czmpatj","cfcho","ojpxp","gwrvruh","tzmhp","jvlsi","cwhfqv","wjeacnw","lfmocar","vdnpxm","htloshw","vtnfxca","bxgcds","hacrmsq","mrtln","steeehx","ovwcp","ekgvd","lzouyx","drqxr","rznae","lkhrq","ytfbtbh","uihyz","wzfou","azqxhfa","ldwngg","paapbfl","xqeyn","dugnd","zdneea","ucdfmor","pjszapd","ynzyb","dciykti","ozhetsh","bncsis","iqifeg","jvdzs","rioonjm","ctdzyi","bvkvnm","eoyuqx","spndso","swfvp","qxzpzh","zyzoaao","zmrevxc","cuonf","ralrh","fznkr","bhloz","dmchxg","xxrctwd","awgkx","armcp","xepxjz","llkhr","vhybi","wljmb","hoksfnr","izdrim","elayhz","xadqrhf","qmekkxk","telcio","oogncjk","rwgiqet","ytwnyh","ibkpdhs","fizvj","lwtjqyq","unxox","uyqpexv","jcdnjsj","xvtnoag","lgnisb","ojruuwy","wrltb","cwamr","efesent","tzwzgxg","jyxcew","hveoxe","pkpftga","pwxxtze","wmbymvi","xlijl","wxaiv","ubgly","birpn","dfkvvgl","aglukoa","resmqsm","kvmyfor","rodtrvu","cnnghvy","xxwok","fzdeub","aicipnf","hopdpr","moynvy","uluovbi","qycyntt","wazlat","eiekwl","zloiely","jfwldm","xmpwra","uxcixl","ltfndn","gdibz","mmdmpx","jstdv","lhveb","rkwmii","oruqb","axkmxb","ilsqgk","fxsln","pqnkol","xlnfus","wafys","gnpzc","vtzdze","nakdc","sghjar","xuxye","hghcjr","jybnhix","inlxmr","illai","gjaro","kmybdp","nzgckm","tmnitcr","dgxyev","qlsohca","fjddhbj","wzrekc","ldbyx","qmzzy","kxnvlwg","oxvarb","xoldv","ayfobnz","puedueg","fxtqbgb","upydow","kacoy","aimbzv","sbwbabw","cccotfx","lbdnn","geynm","nzvai","abyeqr","mpjteij","kdjebup","oafbiw","nnoaszy","pompou","udkifcz","spxsc","kfsingh","afsyxi","fodaynq","dqssvc","uqyiyw","ttqvfa","bfula","fraws","rwrshc","qwyxmc","qhplxbl","wvtfru","vkclnly","kbqqt","phxzxw","gkavk","nxwpnne","ipciny","ptled","qtvxbee","uxpttjj","enaohu","ywxlvls","kcpct","rvqfjn","gvgvus","yrtdudj","bkzyqe","vlqdx","hmkkb","rhkwfng","svbpkhq","iazjqfe","ygnxi","xztdw","habnlb","efdmzt","exksydy","dhmpy","havrwji","vrlksz","wbmaew","iwccxa","swhjtd","ipcqac","dcmdj","fkteig","zkrtzse","cpood","qqyuusw","lifeq","napdq","koywsrd","cagtars","zlhrqt","fnbex","saakf","wtixa","xooszlp","lohko","qnmnr","oqtjqct","fhjpkno","jgoyztd","qgzbcg","lpqat","axswe","gcyoi","jfteuj","oelkjcf","qsapker","hxomlpx","anhkse","zkwjtq","luprb","vgynn","pvtiwac","psgkm","lxniaqo","gplut","jbvvaq","llbjrg","wsorr","dfnhm","oenwp","robjrmb","grambir","bdvlt","qfoze","cpybdc","qkmtej","xpavhka","kmleq","tkrgrq","gmqqx","eoqdq","chtjny","eedbogs","bqropjp","aeksdr","wgqxgy","jocnfw","wcdyky","msxkyqq","rxwada","vbnknuv","tbtocgk","nkivu","vcbexx","onqzp","sobeifr","fphkfoe","wuvihd","mteqv","edjhop","atmuea","civnu","ptrqppv","lwutsc","tnfzoi","twsvtss","tjqfgq","utcvsi","vowcxe","slltp","ghhabl","apbpcx","dshvwr","ljpwo","xezalh","hkhqf","xjklz","sjjju","rsitgp","yyexria","ustbzk","lbvaan","hjhnj","xzjzv","sifdir","iuxwmb","pvvuue","sfafoqy","yahnr","bynaho","jfmwcu","dwpqlgd","wfsliia","wthjpnt","jopxmxa","hilzna","kzeugi","prtvso","pgafhr","annnow","cnhhci","neqbseu","ekstwh","wdmkqg","kihqj","juqcbk","npnwljo","briihw","cyoadq","rrnds","cfebyq","ndifi","nlsus","mktrmhi","lrvhekh","aswoeyt","dmlrhz","jcchjv","kxbcb","vimpfvn","ovbhzxv","svefcvi","tuubk","oosje","xiblz","slxscey","rphmd","vzrso","ikbzx","plvviy","zsjih","liykjrp","tixtmb","gnociw","dofzqe","xmfapi","rxlto","smvmjq","eozvp","ykhod","puhiku","zprexjm","prrfddv","nbxpozw","wjbgjj","qoium","xuyolvr","vgdtip","lgbiwz","dsmewj","mqzzqep","ulunezs","vhfiwd","pzewyn","pmfcz","cctah","flwwez","dvzfpk","jpuclre","kzgnp","rcrldbr","bdhnypo","lpchen","gvnmdvd","awaug","pijjbf","htteulj","nrfhs","ugjdld","simoqtd","vosqg","tyaic","atjnj","dpxctl","ggrxmb","snbum","oeynvo","zhgncsj","jpwwf","bsjyzno","hhsivop","qlhhgit","mnguk","arzrmd","skpikb","jupufi","lzapf","drpzq","wvazs","ygamfns","mdmeyhw","bcwbw","gegng","lturgmj","bgkkt","ziykfr","giatw","gipfvbj","fivtu","nvvfx","vbhhu","shfaz","zmokqk","rgezgl","zcgwau","rssyup","dyucbu","hsdnt","klimami","tagygk","iiwrtoi","nojxfcd","jjlhw","hpfxxh","wzerek","vrhok","bhcss","uovwlf","dcdvg","arsws","uexamps","jsncjbz","bifyxdy","xsgijng","rztxftn","sqnasq","hnzwepl","jlvyaw","weygaou","hirykq","drslu","zbzwc","qfmjft","kvoofr","mirxul","azcyg","rmtxdom","vookrpp","njzycq","zkqciu","mdets","orlzyyj","xonhlo","rxrhqqa","kepkm","eobrx","jgsfpo","esuwtor","fyltki","aazgdfi","hfgixge","aypkrum","fevlnxw","ashjgv","jolysw","urbgg","nxsdw","dtomii","jklvrlf","lllbuug","qggga","gvtovr","uctgzee","jrzjhp","ytphfwq","wcrvcho","iyracw","yklwe","sjyxf","kjfskzl","codcecd","axlwgx","jnhgjt","madhave","vnisb","mazbni","kmllw","vfdhz","wjgjje","wjgsf","vgnoj","zrqxk","qxkppt","ighjhn","gfnpqo","zefxxv","lgfdf","uloym","fczaqw","ijnlnzq","fknwio","ehmrzc","nyecze","ypchba","qfswad","fcxwgta","hcvkc","yegujbq","sndoyy","xukfx","smkky","wbxkn","avretv","znkdz","uhyiars","czisn","yavzhbn","qrsja","pgsmi","hqqlree","yntbl","ehshw","qphys","jgkeb","mpaesw","wwsnby","hvytb","qyfmo","zjgfzl","jwiotqg","fwmkw","egcubw","sdapb","udtgxf","rtzqf","euaft","dovdgip","nywcuhp","gheylr","ngfwbrm","tekeh","ohasghv","uztqco","mogerx","xthrzir","zwdkv","nollaj","egnxivf","krfsarj","pfyvhn","thbbqmf","uufzyk","lipmzn","npsub","yuvclf","aovflj","bjpzdpd","qxqub","ntrqu","hklbhic","cxuzu","rntxeh","gumpu","lqzobuw","ijfabt","ijgvgb","zpqen","nwvodz","nujkp","lbkksc","cwprfpy","qoqfeom","wtrra","xizykyv","mubnb","oysyle","mtihp","bsqizoc","zjqhprb","odpfd","khreyz","eawha","ukufqh","uyutt","mpwhr","muxyao","cwakal","tdsebni","pircf","eojrnz","wzxzk","deyht","esldreo","okxydx","jualqc","crhnk","jqnhxua","mtafkcs","bsneknf","geinyf","fvkmh","wykzpj","zkpgwu","wtlunuy","nnijk","hdocmnb","fgqgl","vcjndon","vzokd","yzndebc","xfzzwvl","wgmrsjo","pufup","nlwhbcl","pumxfwc","rhylm","gxnrwqa","golprw","eujaou","owothz","mdeqgd","utrfo","magkkcl","thyeswt","onryxwi","hhvbgc","lvfwufh","fxqarg","uyglxvq","dfocn","wwamhh","jjuyx","tjauk","mvrjfld","ldlnfb","bhlqac","obxvfmp","qgakqs","dxccryc","cpkigpp","eskgub","ywqqzdm","gmuryv","xceyue","ejdbfdn","tlwiij","vduiu","cxlkc","lfkif","rrdhui","bvjlao","daxzet","udnwim","cblmqms","thqwrhq","buwge","kqcazdy","ehgiso","dfocey","yqncon","wrzkj","gpsqllm","nmvmmx","qnqdzhj","uoqxh","xjzjsro","jsstv","ajosmuj","flevgew","juixan","juzvxme","jkgax","jmusm","fxprdqq","nncqnj","qlpro","ntknppu","oxuznqu","obxeds","jyfyh","nktffrp","eoqlo","itiesx","zmvxrd","fgmkrvj","fbsssaz","whvdtu","ttdws","gxordf","pqsxjzq","cqugq","caortw","sptxqv","sbokpm","oadfq","owumvj","nknbesn","wkhewxh","vkqadmt","slbmlcw","agqnco","aovnnzy","hawrnc","euxggt","xrmalu","vgsim","utiyins","dzpywo","xxghfwy","jxpfw","gwuki","yfavaoj","njvpsa","oxcmk","wsovhw","wqotxn","omwyp","vfipmk","ifkzxl","tebbf","bpdsnnp","ibcki","utupik","fkmda","ourebu","nhuxq","lujptxf","prshcjf","yehkkii","wvsxefv","ovoff","qjxlks","xxbbrf","xhiqucg","goxmlc","lonlet","eefkv","ucrlbg","gicpaq","urvyr","bxdjtyy","quzmq","hmbny","ionkgm","mgizcub","zlcdt","uwmuvze","tmgffjz","nyujjnj","ewmlkxx","xqmonlx","qhheyz","jvsqta","xfipzuf","kslerm","nafuq","hvbjc","zoexudq","tiyvb","rkzdvqc","dunag","pwigcm","znqbimy","mjfiprq","fjgml","djjap","osxctu","bqlviir","rxrkkd","bvsts","bbcsua","acqipex","cdcxqf","uprefr","zzivpzj","ixdux","esfhx","blmdcr","jutggnj","nebredx","mfzree","bxxnuc","xktpy","nygkkp","yealh","nflgr","fljajzb","mxfizr","tayyyo","pbquru","funsc","klqktnn","szaec","zqngj","fqhot","mjvzhik","zcebk","tddfcp","yserhmh","remluz","wvfthju","zzwer","ljotu","lpfgyee","bribj","vjaypq","doyzxp","wipkyed","pmwyb","qwqvuco","jsumk","xuthgir","achhnao","krgev","sfmeura","svwrko","oenqxy","mnpgbq","jwlhtys","dyacib","innjpq","vkohp","dxnsi","xrzdv","ojemxf","aftbnhh","rsdqj","mqklbm","dbytrtf","eosmidu","aitrngj","gzmnqfe","anftt","wxqekx","qghyj","yhifr","qqfbttb","kfihu","qarnqfd","yfstml","zyeejqd","gbpnojp","qepavlt","ltcact","kjefzv","wrlkqu","owcdnpw","ncolrnf","itvazio","mswfpxj","wneex","evvpd","wsbjofb","axpfby","jivercx","mybyjsx","dawky","jpxmx","byiuld","tyepw","frofdd","mukkjw","bpsvin","ejromv","byqdq","nsipc","nlvbkeu","gchlym","urair","bmmptca","hrrgsn","sctlhh","acvxcak","xclikzx","knlkp","oybgps","tlasxad","eslrpo","qkquk","plqwp","jzunxxc","hpdnhgl","qaxpimh","rffcalb","tvkljhc","ekhefl","zuvsfp","pdpiur","vysry","ydxrmky","oyybnf","wudrp","wzkiyn","lzioij","bdmtpf","whrlpg","ehyupzq","lzkre","jmzhed","mwocs","pxxlw","vsnmi","awsarb","cuewazk","linau","ojassu","bloenjh","qstxcbu","zifwp","ajwndug","wpmhw","yttatc","kcqwxfu","jjafri","bzmdq","qlzibo","qmacvr","sqcjig","tzapdy","bjclnm","mrsbh","xwnvxg","bzeebb","kgcrq","ogdpxq","zuaji","lqwwf","qeahabs","acvovfs","glcrcg","jjitme","hpursna","cxqyyr","jmjdyt","gshet","lmqqb","hhstzqz","zxpbe","ojvueor","xpsina","jrxsw","wzjvk","hlbnxvp","orktmbu","ucvlyi","kupkgp","mdttadt","cqvkh","amjkw","nezlb","evhnzfw","tpozdav","popnmu","ebebda","dwiikup","kabor","bwxdj","fdwjanv","cztog","hcdpga","hfpxf","tlqkd","heubybw","wupren","nupiw","hjshep","tpoaimq","patlfo","ltydfcq","wpkux","spingwj","qlzrqhv","zijyib","zstsz","yinejw","rseyc","yzoia","hkjocco","xbkvpd","vqmba","xfiajgi","davquv","onysn","blfis","gmmejm","ovgfyl","ivesp","pqrepbq","sgvkhsr","kdvcup","jutjdaa","gmmvyhu","dioood","jwzha","udofw","yaxsqlj","uipvum","wiethh","ezsclu","hwbto","rjymil","dtcvcum","goqkbx","rnzow","qsdqap","zbiur","yvnin","yuegepx","chgtn","dwtwt","kfrumh","nnmqm","advqqio","leyeu","frqpi","wkclgz","drbsg","ftkbof","opinr","klmus","dyywl","duirjcm","uzfwpvq","ovxxju","xrvsfpb","trtdpzv","kpzfffe","djujla","wjtptw","bzwtmt","lkhvkku","nziiwmc","mlxsar","bcbuz","azssj","dxyvk","bypnce","vzkmjmv","elwybn","kqvpjmk","sdhfs","hcggbd","mhecd","gpcgr","uczya","jikszds","nxfzsl","vqszya","wcatmsf","izrmtzf","jqiyule","agpkrm","exuxawf","blugq","uhscstj","gbawqu","mhftvy","oeszfy","yiuzpi","lgvaik","nesnns","qsoiwom","ssnjwyi","fapbylo","ldazgw","xxnazqu","ghoeqb","zakot","aiqnywv","aqifhm","mbyisor","amavv","rgritfd","myhdhl","orewkt","xqoanm","oonznow","bisln","zqxezgc","tqwya","pwageyt","aqkebq","pzmjj","vipeypu","woncgt","qzbeia","wujhr","hnzfi","nbaqwpm","rscjyaz","rrpys","flrib","erzhjwk","kpkyi","ooxwkmc","bmwnw","dqdfdn","jabup","hyjfqf","kfdyk","eumjmb","koprevn","lbpzror","caxit","nndqha","rvgrrx","rcawf","kqdvfln","wsyqd","xoghe","kwnbw","qoqtvsv","yepxefp","pwlpz","kkajk","tauqbt","tzfqcm","oaakfr","lxycdb","suaiprq","vgiois","uugeq","uicgill","llninoh","ylpjh","ehdcs","niqpr","yyugsu","evticix","rgezka","zrzelf","xmiyoln","pitfs","pzlsmix","booky","qvwchgy","pxjzy","rtwcx","laigm","vbvjp","ehjqyyw","fabof","afsfvuc","quutr","qscptos","abedhcj","mhflla","tdyyan","vpbgnaz","kmjziz","nttxob","ppwgj","sjtgr","qyofye","nmfaq","axrohcv","zwzznb","ikikoay","brepugm","dasppn","kxyuazi","tammsgv","ifliqg","obttzfq","iamrgv","vzzuci","upjotu","ynngde","kingmk","rbvaxmb","njnmjky","ukanr","jldtvu","ghbmr","aojsj","fdurvg","ponokvw","lopznq","bflwxru","fsjzao","fumjd","odxkcd","zibtvs","fzfsbge","flyckw","uvbxhw","mscxirg","bxwcw","idlbsx","jkcjkq","uhfll","feprium","vtukxal","cdpgjlt","yzwug","alxlp","jxamt","dxzjsjz","pusjjs","saxfhz","wyngbu","zlvahe","qyjly","chsaxj","ozbnsrv","nkvtdi","pwqlj","vhifz","fmjlun","ydyaho","llbfvj","nxowdx","vuaqls","fbwlicd","mrohqw","xldxgwb","qzgxxpc","cevvo","lwsuuak","ncgzj","ngiqiqe","oacoqol","ttyzz","docyy","kyevjkr","etbjhx","ozknejo","ypmby","ssborpf","wsvicoo","sjhtn","wcrnim","ysrprwj","dsiod","ocyqxuo","nijge","ikeoeu","rbysqkn","ajjcy","uzpabx","alesft","decepk","auzgqs","njtqz","wvbdlup","sgxjq","oblrltx","bhozx","lmjdqk","jezhz","jlohp","gqvva","vdamjgt","imisbp","hmqga","urlxfjj","stbluhs","irfuej","owrnytn","ptrzz","eojccog","xjehcay","qsggxwe","kxryq","ldkak","aribcv","qtanel","xrhajw","biimx","mkxdu","ndlzt","ectcyi","kymmxu","zanrzol","yrqibx","jfdidh","ebhas","atjtek","ykjdy","qkmhygb","ckzex","rxeur","tpthp","hjcby","ycbsv","urbtz","lqsssud","txygpu","togekcq","whymkv","wyvwko","bwrfv","whqrzih","eebsen","nxycv","kdnwp","luctxhn","wkjcx","ufohqlv","isdodl","yjvxys","wukdfv","uxgwce","jkfkaz","wjudgi","irhvei","poughh","fdmozyp","wgnwl","bsuksw","gwvhlh","siptftx","iatus","bbbkr","bwzwo","uflhzyw","lofvgi","xhkyx","disqvl","vamyr","smzcux","kwwjca","buddupq","tkjuef","jxxggu","szgszdh","jrnocr","jevdn"]))
# print(minimumLengthEncoding(["time", "atime", "btime"]))
'''
import math
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
target = 4
ans = []
Tar = target
TempTar = 0
while True:
    for edge in edges:
        if edge[1] == Tar:
            TempTar = edge[0]
    count = 0
    for edge in edges:
        if edge[0] == TempTar:
            count += 1
    ans.append(count)
    Tar = TempTar
    if Tar == 1:
        break
probability = 1/(math.prod(ans))
print(probability)

