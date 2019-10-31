"""
3 kyu - Fabergè Easter Eggs crush test

that takes 2 arguments - the number of eggs n and the number of trys m -
you should calculate maximum scyscrapper height (in floors),
in which it is guaranteed to find an exactly maximal floor from which that an egg won't crack it.

Which means,

0. You can throw an egg from a specific floor every try
1. Every egg has the same, certain durability - if they're thrown from a certain floor or below, they won't crack.
Otherwise they crack.
2. You have n eggs and m tries
3. What is the maxmimum height, such that you can always determine which floor the target floor is
when the target floor can be any floor between 1 to this maximum height?

"""


dic = {}


def height(n, m):
    if n == 0 or m == 0:
        return 0
    elif n >= m:
        return (2 ** m) - 1
    elif n == 1:
        return m
    elif n == 2:
        return ((m ** 2) + m) // 2
    elif (n, m) in dic:
        return dic[(n, m)]

    res = 1 + height(n, m - 1) + height(n - 1, m - 1)
    dic[(n, m)] = res
    return res


if __name__ == "__main__":
    old_recursion_limit = sys.getrecursionlimit()
    print(old_recursion_limit)
    sys.setrecursionlimit(10000)

    print(height(0, 14), 0)
    print(height(2, 0), 0)
    print(height(2, 14), 105)
    print(height(7, 20), 137979)

    print(height(7, 500), 1507386560013475)
    print(height(237, 500),
                       431322842186730691997112653891062105065260343258332219390917925258990318721206767477889789852729810256244129132212314387344900067338552484172804802659)
    print(height(477, 500),
                       3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127420959866658939578436425342102468327399)

    print(height(477, 10000),
                     600461396604105297697414530102187796624607351959572356167325648574309381899274255809992726647041509608874296502550889633566626669839693460163703754386982346596293491455058459167135769401101845748849154474806919582238098292865002615140455747337045606515913175800206705264197158348258877027342824497813598887212567460615138259041983561196905824547148562128771846272230901329804068790524523450526723439711852711480043539388255029594388405065227411436195811544328549172691557810516507323615400468586962803403389031164507526999175383227883564967859574994520910983381843074859047295120948531800868902878466257920126328541103471268056861774184467685136934882998123768531695075047132113902537018783846627502099156246969377215926174782697180458326177412430190794351610099943109019040476655865297322723014683870220977314898596096355345407775)
    # print(height(4477, 10000),
    #                    1322821654800439589583624607836730988904348989635184483838675315989863014466105368917516854788173412697117838413572154358020136361352589223655004309284002331356645126308444045548293566543482035130766876362770186754407172004758665811853489554425555053643908845358225658078400880897420458613361537230692347145029937146468449752350301582966318881236041448346697864308936041807973848575815961020957973841925430394889030910761307668821228255147323012321726504304076902912463702108956669795566661303469766408411346447369441900601416549889768545415835808703102634187636408616862788628220968336302080405978291461615690517333300338026427209023338744576796796711916921553117367799805818262372383440027895158535027538219368128415201884328355249194560412959735085368099726719812587209832125121706467856448219467001478841957398661311948630752866817235891668491371246314423172093241855801986462213764272472077704090737449586014952207200402488115806480036391258788025058712927761809494607747190593544252498024965313654475511753397288550572364193751016698751124385432059855618738610770405495965628076729605040379761490680887446751742893838217109555332410367754941969641188014103364853464553866605149284789373350284278475702952002720219396744665142719739890709306702230989773403063833223142722153866753072260856577382714941017978371516349454986201414282722361391051916542589551016023190730497041390846243435703142324656990673688597131961469432804559244656573403972845547140551161388227163311600434649131672174329566859257640294347413250504689740356122993141714018763824536995756394554473053764885655217850919825484110456823718017936279926312676444075372513295121643005522507990093614688397324087158672285564265461960725048409644632356562813282311892621316990617791305949952474644973231563181802912551788866587392922962344851922680688121341506499860485837386801968860995052055236149946250164753714765692652499211749864280505191012859114807502067989910205943513218116464920029858713308646212996605582239145947185971138791937105763767017369327250323372490209312303407044663140291579276982729680418229917148740734819240902048630120317091983651644063173722960555978628497587823422375493107579742775550922433788067185239451798388809414158837037653589325259023780409914069533039705450496176647169891013697813337588075535112140970187607803915384622627522925822608742766549203712747041753891038754047696049037861483951837513375322742464580059309440669921941688909946789319835787709445925359884114002203388057590959620340874700472926972472437928806956105916022048677333952506175442513146994611155259594220312914080066998804113859428782103809127996851589054428051854854318799508483531803897517007935349549152870011407064621017082135138020750461696192841200272984193298057507960103670538167626863921460268009725329427763452347838828602301814121408102409549978991436252168617142842111215900368726060166926158698664478612916125923479260041837538259289930459928491560009034059912265253387804412611357982786191578331327)
    # print(height(9477, 10000),
    #                    19950631168807583848837421626835850838234968318861924548520089498529438830221946631919961684036194597899331129423209124271556491349413781117593785932096323957855730046793794526765246551266059895520550086918193311542508608460618104685509074866089624888090489894838009253941633257850621568309473902556912388065225096643874441046759871626985453222868538161694315775629640762836880760732228535091641476183956381458969463899410840960536267821064621427333394036525565649530603142680234969400335934316651459297773279665775606172582031407994198179607378245683762280037302885487251900834464581454650557929601414833921615734588139257095379769119277800826957735674444123062018757836325502728323789270710373802866393031428133241401624195671690574061419654342324638801248856147305207431992259611796250130992860241708340807605932320161268492288496255841312844061536738951487114256315111089745514203313820202931640957596464756010405845841566072044962867016515061920631004186422275908670900574606417856951911456055068251250406007519842261898059237118054444788072906395242548339221982707404473162376760846613033778706039803413197133493654622700563169937455508241780972810983291314403571877524768509857276937926433221599399876886660808368837838027643282775172273657572744784112294389733810861607423253291974813120197604178281965697475898164531258434135959862784130128185406283476649088690521047580882615823961985770122407044330583075869039319604603404973156583208672105913300903752823415539745394397715257455290510212310947321610753474825740775273986348298498340756937955646638621874569499279016572103701364433135817214311791398222983845847334440270964182851005072927748364550578634501100852987812389473928699540834346158807043959118985815145779177143619698728131459483783202081474982171858011389071228250905826817436220577475921417653715687725614904582904992461028630081535583308130101987675856234343538955409175623400844887526162643568648833519463720377293240094456246923254350400678027273837755376406726898636241037491410966718557050759098100246789880178271925953381282421954028302759408448955014676668389697996886241636313376393903373453647052103349469928076954249980154345544196049720110441880956939571653303125965015135210943821418326301263747755849915390311849600620405839184806696574011638771223876684308393546154357007879197176278577010897776871509293312271446308325915207411683581162864877565099831828100966285215817182861422299916721214461558309048173509038700144141092935627106729962305873603830938160653941875633254649208486247541063094454500007666144426589865904402944100565434252161641454059574448959059378469034843694065251975339636452128242737679086169540365161261103781301842588718151775952124493692901275351280453566829099730411742607415703660912889996893392281666409912913934377489142688784235343954049469043333120897248862080530937185907276885584072254792345533781517753151320818102507950307194516201547412495983145614252402137833853984659077543542376699008277188650448599930163536123001047126485885945475644)
    #


    sys.setrecursionlimit(old_recursion_limit)