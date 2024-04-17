
custom_field_types = [dict,list,str,int,float,bool]#,type(None) should have already exited if none


#NAMES
non_alpha_characters_to_exclude = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", "[", "]", "{", "}", "|", 
    "\\", ";", ":", "\"", "'", "<", ">", "/", "?", "~", "`"
]
name_suffixes = [
  'jr', 'sr', 'ii', 'iii', 'iv', 'v'
]

meged_normalize_honorifics = {
    'jr':"Jr.",
    'sr':"Sr.",
    'ii':"II",
    'iii':"III",
    'iv':"IV",
    'v':"V",

    "mr":"Mr.",
    "ms":"Ms.",
    "mrs":"Mrs.",
    "miss":"Miss",
    "professor":"Professor",
    "doctor":"Doctor",
    "rep":"Representative",
    "representative":"Representative",
    "pres":"President",
    "madam":"Madam",
    "madame":"Madame",
    "sir":"Sir",
    "sen":"Senator",
    "senator":"Senator",
    "mister":"Mister",
    'dr': "Dr.",
    'prof': "Professor",
    'rev': "Reverend",
    'pastor': "Pastor",
    'bishop': "Bishop",
    'archbishop': "Archbishop",
    'hon': "Honorable",
    'dean': "Dean",
    
    # Military titles
    'gen': "General",
    'ltgen': "Lieutenant General",
    'majgen': "Major General",
    'col': "Colonel",
    'ltcol': "Lieutenant Colonel",
    'maj': "Major",
    'capt': "Captain",
    'lt': "Lieutenant",
    'sgt': "Sergeant",

    # Governmental and official titles
    'gov': "Governor",
    'sen': "Senator",
    'rep': "Representative",
    'pres': "President",
    'vp': "Vice President",
    'judge': "Judge",

    'prof': "Professor",
    'assocprof': "Associate Professor",
    'asstprof': "Assistant Professor",
    'lect': "Lecturer",
    'senlect': "Senior Lecturer",
    
    # Medical and healthcare titles
    'md': "MD",
    "do":"DO",
    'phd': "PhD",
    'dds': "DDS",
    'esq': "Esq",
    'pharmd': "PharmD",
    "pharm d":"PharmD",
    'crna': "CRNA",
    'rn': "RN",
    'np': "NP",
    'pa': "PA",
}

suffix_normalize = {
    'jr':"Jr.",
    'sr':"Sr.",
    'ii':"II",
    'iii':"III",
    'iv':"IV",
    'v':"V"
}

normalize_prefix = {
    "mr":"Mr.",
    "ms":"Ms.",
    "mrs":"Mrs.",
    "miss":"Miss",
    "professor":"Professor",
    "doctor":"Doctor",
    "rep":"Representative",
    "representative":"Representative",
    "pres":"President",
    "madam":"Madam",
    "madame":"Madame",
    "sir":"Sir",
    "sen":"Senator",
    "senator":"Senator",
    "mister":"Mister",
    'dr': "Dr.",
    'prof': "Professor",
    # Religious titles
    'rev': "Reverend",
    'fr': "Father",
    'sr': "Sister",
    'br': "Brother",
    'pastor': "Pastor",
    'bishop': "Bishop",
    'archbishop': "Archbishop",
    
    # Honorary and academic
    'hon': "Honorable",
    'dean': "Dean",
    
    # Military titles
    'gen': "General",
    'ltgen': "Lieutenant General",
    'majgen': "Major General",
    'col': "Colonel",
    'ltcol': "Lieutenant Colonel",
    'maj': "Major",
    'capt': "Captain",
    'lt': "Lieutenant",
    'sgt': "Sergeant",

    # Governmental and official titles
    'gov': "Governor",
    'sen': "Senator",
    'rep': "Representative",
    'pres': "President",
    'vp': "Vice President",
    'judge': "Judge",

}


normalize_titles = {
    # Academic and professional titles
    
    'prof': "Professor",
    'assocprof': "Associate Professor",
    'asstprof': "Assistant Professor",
    'lect': "Lecturer",
    'senlect': "Senior Lecturer",
    
    # Medical and healthcare titles
    'md': "MD",
    "do":"DO",
    'phd': "PhD",
    'dds': "DDS",
    'esq': "Esq",
    'pharmd': "PharmD",
    "pharm d":"PharmD",
    'crna': "CRNA",
    'rn': "RN",
    'np': "NP",
    'pa': "PA",
}

normalize_prefix = {
    'mrs': "Mrs.",
    'mr': "Mr.",
    'gov': "Governor",
    'principal': "Principal",
    'prof': "Professor",
}

common_employers = {
    "freelance":"Self Employed",
    "none":"Not Employed",
    "me":"Self Employed",
    "n/a":"Not Employed",
    "na":"Not Employed",
    "nothing":"Not Employed",
    "nada":"Not Employed",
    "n\a":"Not Employed",
    "unemployed":"Not Employed",
    "myself":"Self Employed",
    "me":"Self Employed",
    "not-employed":"Not Employed",
    "us government":"Federal Government",
    "ms.":"Microsoft",
    "sel employed":"Self Employed",
    "self - employed":"Self Employed",
    "Self / Consulting ( Tax & Legal )":"Self Employed",
    "self-emoloyed":"Self Employed",
    "self-employed contractor":"Self Employed",
    "selk":"Self Employed",
    "ms":"Microsoft",
    "a bank":"Banking",
    "apple":"Apple Inc.",
    "apple inc":"Apple Inc.",
    "apple, inc.":"Apple Inc.",
    "state of ca":"state of california",
    "ey":"Ernst & Young",
    "us govt":"Federal Government",
    "ohsu":"Ohio Health & Science University",
    "duke":"Duke University",
    "harvard":"Harvard University",
    "harvarduniversity":"Harvard University",
    "u harvard":"Harvard University",
    "harvardu":"Harvard University",
    "- select -":None,
    "20th century fox entertainment":"20th Century Fox",
    "20th century fox television":"20th Century Fox",
    "20th century fox tv":"20th Century Fox",
    "your mom":None,
    "yelp, inc.":"Yelp",
    "yelp, inc":"Yelp",
    "yale univ.":"Yale University",
    "yale":"Yale University",
    "cannot disclose":None,
    "cant disclose":None,
    "cant say":None,
    "cannot say":None,
    "can't say":None,
    "can't disclose":None,
    "secret":None,
    "private":None,
    "none of your business":None,
    "confidential":None,
    "confidential.":None,
    "confidentiality":None,
    "its a secret":None,
    "its confidential":None,
    "it's confidential":None,
    "its private":None,
    "it's private":None,
    "it's secret":None,
    "it's a secret":None,
    "its secret":None,
    "private company":None,
    "xx":None,
    "xxx":None,
    "xxxx":None,
    "xxxxx":None,
    "xxxxxxx":None,
    "xxxxxxxxx":None,
    "xyz":None,
    "work":None,
    "own":"Self Employed",
    "own business":"Self Employed",
    "aelf":"Self Employed",
    ".self":"Self Employed",
    "self":"Self Employed",
    "self employed":"Self Employed",
    "self-employed":"Self Employed",
    "self.":"Self Employed",
    "retired":"Retired",
    "none":"Not Employed",
    "not employed":"Not Employed",
    "not-employed":"Not Employed",
    "can't say":None,
    "dep":None,
    "@properties":None,
    "a big company":None,
    "a company":None,
    "amounts=5,10,25,50,100,150,250":None,
    "asd":None,
    "asdf":None,


    "latham & watkins llp":"Latham & Watkins LLP",
    "a hospital":"Hospital",
    "a health insurance company.":"Health Insurance",
    "depaul":"Depaul University",
    "depaul university":"depaul university",
    "department of veteran affairs":"Department of Veterans Affairs",
    "department of veterans afairs":"Department of Veterans Affairs",
    "department of veterans affairs":"Department of Veterans Affairs",
    "dep’t of commerce":"Department of Commerce",
    "citi":"Citi",
    "citi group":"Citi",
    "citibank":"Citi",
    "citibank na":"Citi",
    "cisco systems":"Cisco Systems",
    "cisco systems inc":"Cisco Systems",
    "cisco systems, inc":"Cisco Systems",
    "cisco systems, inc.":"Cisco Systems",
    "cincinnati children's":"Cincinnati Children's Hospital",
    "cincinnati children’s":"Cincinnati Children's Hospital",
    "cincinnati children's hospital":"Cincinnati Children's Hospital",
    "cigna":"Cigna",
    "cigna healthcare":"Cigna",
    "christiana care":"Christiana care",
    "christiana care health system":"Christiana care",
    "christianacare":"Christiana care",
    "chipotle":"Chipotle Mexican Grill",
    "chipotle mexican grill":"Chipotle Mexican Grill",
    "children's mercy":"Children's Mercy Hospital",
    "children’s mercy":"Children's Mercy Hospital",
    "children's mercy hospital":"Children's Mercy Hospital",
    "children’s mercy hospital":"Children's Mercy Hospital",
    "children’s mn":"Children's Mercy Hospital",
    "childrens hospital harvard med sch":"Children's Hospital Harvard Medical School",
    "chiesa shahinian & giantomasi":"Chiesa Shahinian & Giantomasi PC",
    "chiesa shahinian & giantomasi pc":"Chiesa Shahinian & Giantomasi PC",
    "chevron corporation":"Chevron",
    "chase bank":"Chase",
    "charles schwab":"Charles Schwab",
    "charles schwab & co., inc.":"Charles Schwab",
    "ceo":"CEO",
    "century link":"CenturyLink",
    "centurylink":"CenturyLink",
    "centura":"Centura Health",
    "centura health":"Centura Health",
    "centrify":"Centrify",
    "centrify corporation":"Centrify",
    "centers for medicare & medicaid services":"Centers for Medicare & Medicaid Services",
    "centers for medicare and medicaid services":"Centers for Medicare & Medicaid Services",
    "center on budget and policy priorities":"Center on Budget and Policy Priorities",
    "center on budget/policy priorities":"Center on Budget and Policy Priorities",
    "cedars sinai":"Cedars-Sinai",
    "cedars sinai medical center":"Cedars-Sinai",
    "cedars-sinai":"Cedars-Sinai",
    "cedars-sinai medical center":"Cedars-Sinai",
    "cbs studio center":"CBS Studios",
    "cbs studios":"CBS Studios",
    "cbs corp":"CBS",
    "cbs corporation":"CBS",
    "cbs television":"CBS",
    "cbs television studios, inc.":"CBS",
    "cbs tv":"CBS",
    "cbs tv studios":"CBS",
    "cbre, inc.":"CBRE",
    "caterpillar":"Caterpillar",
    "caterpillar inc":"Caterpillar",
    "caterpillar inc.":"Caterpillar",
    "cast & crew":"Cast and Crew",
    "cast and crew":"Cast and Crew",
    "caramba inc":"Caramba Inc",
    "caramba inc.":"Caramba Inc",
    "caplin & drysdale":"Caplin & Drysdale",
    "caplin & drysdale, chtd.":"Caplin & Drysdale",
    "capitol counsel":"Capitol Counsel",
    "capitol counsel llc":"Capitol Counsel",
    "capital one":"Capital One",
    "capital one financial":"Capital One",
    "cambridge univ press":"Cambridge University Press",
    "cambridge health alliance and self":"Cambridge Health Alliance",
    "cambridge associates":"Cambridge Associates",
    "cambridge associates llc":"Cambridge Associates",
    "cal. teachers assn":"California Teachers Association",
    "california state university, stanislaus":"California State University Stanislaus",
    "california state university, sacramento":"California State University Sacramento",
    "cal state u monterey bay":"California State University of Monterey Bay",
    "california state university, northridge":"California State University Northridge",
    "cal state univ northridge":"California State University Northrdige",
    "california state university, east bay":"California State University East Bay",
    "california state univ, chico":"California State University Chico",
    "california state univ., chico":"California State University Chico",
    "california state university chico":"California State University Chico",
    "california state university, chico":"California State University Chico",
    "cal state":"California State University",
    "cal state univ":"California State University",
    "cal state univ./self":"California State University",
    "cal state university":"California State University",
    "cal state san marcos":"California State San Marcos",
    "cal state fullerton":"California State Fullerton",
    "cal state east bay":"California State East Bay",
    "cal poly":"California Polytechnic State University",
    "cal poly slo":"California Polytechnic State University",
    "cal poly san luis obispo":"California Polytechnic San Luis Obispo",
    "cal poly pomona":"California Polytechnic Pomona",
    "calif. dept. of rehabilitation":"California Department of Rehabilitation",
    "california doj":"California Department of Justice",
    "univ of calif. hastings college of law":"University of California, Hastings College of Law",
    "cahill gordon & reindel":"Cahill Gordon & Reindel",
    "cahill gordon & reindel llp":"Cahill Gordon & Reindel",
    "caesar's entertainment":"Caesars Entertainment",
    "caesars":"Caesars Entertainment",
    "caesars entertainment":"Caesars Entertainment",
    "caci":"CACI",
    "caci inc":"CACI",
    "deloitte consulting":"Deloitte",
    "fuck":None,
    "shit":None,
    "caci international":"CACI",
    "butte-glenn ccd":"Butte-Glenn Community College District",
    "butte-glenn community college district":"Butte-Glenn Community College District",
    "butler snow":"Butler Snow LLP",
    "butler snow llp":"Butler Snow LLP",
    "bush gottlieb":"Bush Gottlieb",
    "bush gottlieb et al.":"Bush Gottlieb",
    "buchanan ingersoll & rooney":"Buchanan Ingersoll & Rooney",
    "buchanan ingersoll & rooney pc":"Buchanan Ingersoll & Rooney",
    "bryan cave":"Bryan Cave LLP",
    "bryan cave leighton paisner":"Bryan Cave LLP",
    "bryan cave leighton paisner llp":"Bryan Cave LLP",
    "bryan cave llp":"Bryan Cave LLP",
    "brownstein":"Brownstein Hyatt Farber Schreck LLP",
    "brownstein hyatt":"Brownstein Hyatt Farber Schreck LLP",
    "brownstein hyatt farber schreck":"Brownstein Hyatt Farber Schreck LLP",
    "brownstein hyatt farber schreck llp":"Brownstein Hyatt Farber Schreck LLP",
    "brownstein hyatt farber schreck, llp":"Brownstein Hyatt Farber Schreck LLP",
    "brownstein hyatt farber schreck,llp":"Brownstein Hyatt Farber Schreck LLP",
    "brownstein/hyatt/farber/schreck":"Brownstein Hyatt Farber Schreck LLP",
    "broward county public schools":"Broward County Public Schools",
    "broward county schools":"Broward County Public Schools",
    "brooklyn college":"Brooklyn College",
    "brooklyn college - retired":"Brooklyn College",
    "brooklyn college, cuny":"Brooklyn College",
    "brooklyn college( cuny)":"Brooklyn College",
    "brooklyn college/cuny":"Brooklyn College",
    "broadridge financial":"Broadridge Financial",
    "broadridge financial solutions":"Broadridge Financial",
    "broadlawns med center":"Broadlawns Medical Center",
    "broadlawns medical center":"Broadlawns Medical Center",
    "broadcom":"Broadcom",
    "broadcom corp":"Broadcom",
    "broadcom corporation":"Broadcom",
    "broadcom inc":"Broadcom",
    "broadcom inc.":"Broadcom",
    "broadcom ltd":"Broadcom",
    "brigham & women's hospital":"Brigham and Women's Hospital",
    "brigham and women's hospital":"Brigham and Women's Hospital",
    "brigham and women’s hospital":"Brigham and Women's Hospital",
    "brigham and women’s hospital boston":"Brigham and Women's Hospital",
    "brigham and womens hospital":"Brigham and Women's Hospital",
    "bredhoff & kaiser pllc":"bredhoff & Kaiser PLLC",
    "bredhoff & kaiser, p.l.l.c.":"bredhoff & Kaiser PLLC",
    "breakthru beverage":"Breakthru Beverage Group",
    "breakthru beverage group":"Breakthru Beverage Group",
    "bracewell":"Bracewell LLP",
    "bracewell llp":"Bracewell LLP",
    "bozeman public schools":"Bozeman Sublic Schools",
    "bozeman school district":"Bozeman Sublic Schools",
    "bozeman school district #7":"Bozeman Sublic Schools",
    "boys & girls clubs":"Boys & Girls Clubs",
    "boys and girls club":"Boys & Girls Clubs",
    "box":"Box",
    "box inc":"Box",
    "box, inc":"Box",
    "boston scientific":"Boston Scientific",
    "boston scientific corporation":"Boston Scientific",
    "boston children's hospital":"Boston Children's Hospital",
    "boston children’s hospital":"Boston Children's Hospital",
    "boston childrens hospital":"Boston Children's Hospital",
    "boston beer co":"Boston Beer Co",
    "boston beer company":"Boston Beer Co",
    "booz allen":"Booz Allen Hamilton",
    "booz allen hamilton":"Booz Allen Hamilton",
    "booz allen hamilton inc":"Booz Allen Hamilton",
    "booz allen hanilton":"Booz Allen Hamilton",
    "booze allen hamilton":"Booz Allen Hamilton",
    "bond schoeneck & king":"Bond, Schoeneck & King",
    "bond, schoeneck & king":"Bond, Schoeneck & King",
    "boies schiller flexner llp":"Boies Schiller Flexner LLP",
    "boeing":"Boeing",
    "boeing company":"Boeing",
    "board of ed":"Board of Education",
    "board of education":"Board of Education",
    "bank of america":"Bank of America",
    "bank of america merrill lynch":"Bank of America",
    "bofa":"Bank of America",
    "banfield":"Banfield Pet Hospital",
    "banfield pet hospital":"Banfield Pet Hospital",
    "baltimore city public schools":"Baltimore City Public Schools",
    "baltimore city schools":"Baltimore City Public Schools",
    "ballard spahr":"Ballard Spahr LLP",
    "ballard spahr llp":"Ballard Spahr LLP",
    "ball":"Ball Corporation",
    "ball corporation":"Ball Corporation",
    "baker hostetler":"BakerHostetler",
    "baker hostetler llp":"BakerHostetler",
    "bakerhostetler":"BakerHostetler",
    "baker botts l.l.p.":"Baker Botts LLP",
    "baker botts llp":"Baker Botts LLP",
    "baker & mckenzie":"Baker & McKenzie LLP",
    "baker & mckenzie llp":"Baker & McKenzie LLP",
    "baker & hostetler":"Baker & Hostetler LLP",
    "baker & hostetler llp":"Baker & Hostetler LLP",
    "bain & company":"Bain & Company",
    "bae systems":"BAE Systems",
    "bae systems inc":"BAE Systems",
    "bae systems, inc.":"BAE Systems",
    "b2k social ventures":"B2K Social Ventures",
    "b2k social ventures llc":"B2K Social Ventures",
    "a bank":"Banking",
    "axinn, veltrop & harkrider":"Axinn, Veltrop & Harkrider",
    "axinn, veltrop & harkrider llp":"Axinn, Veltrop & Harkrider",
    "avalon risk llc":"Avalon Risk, LLC",
    "avalon risk, llc":"Avalon Risk, LLC",
    "avago":"Avago Technologies",
    "avago technologies":"Avago Technologies",
    "automattic":"Automattic",
    "automattic inc.":"Automattic",
    "autodesk":"Autodesk",
    "autodesk, inc.":"Autodesk",
    "(editor/consultant) author":"Author",
    "aurora health care":"Aurora Healthcare",
    "aurora healthcare":"Aurora Healthcare",
    "augustana college":"Augustana College",
    "augustana college (sd)":"Augustana College",
    "attorney":"Attorney",
    "atrius health":"Atrius Health",
    "atriushealth":"Atrius Health",
    "athenahealth":"AthenaHealth",
    "athenahealth, inc.":"AthenaHealth",
    "at&t":"AT&T",
    "at&t mobility":"AT&T",
    "at&t services":"AT&T",
    "at&t services, inc.":"AT&T",
    "att":"AT&T",
    "astrazeneca":"Astrazeneca",
    "astrazeneca pharmaceuticals":"Astrazeneca",
    "asana":"Asana",
    "asana, inc.":"Asana",
    "artist":"Artist",
    "artist self-employed":"Artist",
    "arnold & porter":"Arnold & Porter",
    "arnold & porter kaye scholer":"Arnold & Porter",
    "arnold & porter kaye scholer llp":"Arnold & Porter",
    "arnold & porter llp":"Arnold & Porter",
    "arnold and porter":"Arnold & Porter",
    "arnold and porter kaye scholer":"Arnold & Porter",
    "arlington county public schools":"Arlington Public Schools",
    "arlington public schools":"Arlington Public Schools",
    "arlington school district":"Arlington Public Schools",
    "arlington countty":"Arlington County",
    "arlington county":"Arlington County",
    "arlington county government":"Arlington County",
    "ark blue cross blue shield":"Ark Blue Cross Blue Shield",
    "arkansas blue cross blue shield":"Ark Blue Cross Blue Shield",
    "argonne nat'l laboratory":"Argonne National Laboratory",
    "argonne national lab":"Argonne National Laboratory",
    "argonne national laboratory":"Argonne National Laboratory",
    "arent fox":"Arent Fox",
    "arent fox llp":"Arent Fox",
    "ardent health services":"Ardent Realty Services, Ltd.",
    "ardent realty services, ltd.":"Ardent Realty Services, Ltd.",
    "arcadia university":"Arcadia University",
    "arcadia university, pa 19038":"Arcadia University",
    "appnexus":"AppNexus",
    "appnexus, inc.":"AppNexus",
    "applied materials":"Applied Materials",
    "applied materials, inc.":"Applied Materials",
    "apple":"Apple Inc.",
    "apple inc":"Apple Inc.",
    "apple inc.":"Apple Inc.",
    "apple, inc":"Apple Inc.",
    "apple, inc.":"Apple Inc.",
    "appleinc":"Apple Inc.",
    "anthem":"Anthem",
    "anthem inc":"Anthem",
    "anthem, inc":"Anthem",
    "anthem, inc.":"Anthem",
    #changing their name one existing example was anthem/elevance health
    "anthem/elevance health":"Anthem",
    "elevance health":"Anthem",
    "elevance":"Anthem",
    "elevance-health":"Anthem",
    "anthem elevance":"Anthem",
    "anthem-elevance":"Anthem",
    "anheuser busch":"Anheuser-Busch",
    "anheuser busch, llc":"Anheuser-Busch",
    "anheuser-busch inbev":"Anheuser-Busch",
    "anheuserbusch inbev":"Anheuser-Busch",
    "anheuser busch inbev":"Anheuser-Busch",
    "anheuser busch":"Anheuser-Busch",
    "ab inbev":"Anheuser-Busch",
    "a-b / inbev":"Anheuser-Busch",
    "ab inbev":"Anheuser-Busch",
    "anne arundel county public schools":"Anne Arundel County Public Schools",
    "analog devices":"Analog Devices",
    "analog devices inc":"Analog Devices",
    "amgen":"Amgen",
    "amgen inc":"Amgen",
    "amgen inc.":"Amgen",
    "amazon":"Amazon",
    "amazon, inc":"Amazon",
    "amazon, inc.":"Amazon",
    "amazon.com":"Amazon",
    "amazon.com customer service":"Amazon",
    "amazon.com, inc.":"Amazon",
    "alzheimer's association":"Alzheimer's Association",
    "alzheimer’s association":"Alzheimer's Association",
    "altshuler berzon":"Altshuler Berzon LLP",
    "altshuler berzon llp":"Altshuler Berzon LLP",
    "alston & bird":"Alston & Bird",
    "alston & bird llp":"Alston & Bird",
    "alphabet":"Alphabet",
    "alphabet inc":"Alphabet",
    "alphabet inc.":"Alphabet",
    "alphabet, inc":"Alphabet",
    "alphabet, inc.":"Alphabet",
    "allstate":"Allstate",
    "allstate insurance":"Allstate",
    "allstate insurance company":"Allstate",
    "aledade":"Aledade",
    "aledade, inc":"Aledade",
    "akin gump":"Akin Gump Strauss Hauer & Feld LLP",
    "akin gump llp":"Akin Gump Strauss Hauer & Feld LLP",
    "akin gump strauss hauer & feld":"Akin Gump Strauss Hauer & Feld LLP",
    "akin gump strauss hauer & feld llp":"Akin Gump Strauss Hauer & Feld LLP",
    "akin gump strauss hauer & feld, llp":"Akin Gump Strauss Hauer & Feld LLP",
    "akerman":"Akerman LLP",
    "akerman llp":"Akerman LLP",
    "akamai":"Akamai Technologies",
    "akamai technologies":"Akamai Technologies",
    "airbnb":"AirBnb",
    "airbnb, inc.":"AirBnb",
    "agm financial services":"AGM Financial Services",
    "agm financial services, inc":"AGM Financial Services",
    "affirm":"Affirm",
    "affirm, inc.":"Affirm",
    "advocate health":"Advocate Health Care",
    "advocate health care":"Advocate Health Care",
    "advocate healthcare":"Advocate Health Care",
    "advocate aurora health":"Advocate Aurora Health",
    "advocate aurora healthcare":"Advocate Aurora Health",
    "advertising":"Advertising",
    "advertising agency":"Advertising",
    "adventist health":"Adventist Health",
    "adventist health system":"Adventist Health",
    "adventist health west":"Adventist Health",
    "adventist healthcare":"Adventist Health",
    "advent health":"Advent Health",
    "adventhealth":"Advent Health",
    "adp":"ADP",
    "adp, llc":"ADP",
    "adobe":"Adobe",
    "adobe inc":"Adobe",
    "adobe inc.":"Adobe",
    "adobe systems":"Adobe",
    "adobe systems inc.":"Adobe",
    "adobe, inc.":"Adobe",
    "admin":"Administrator",
    "administration":"Administrator",
    "administrator":"Administrator",
    "ad hoc":"Ad Hoc",
    "ad hoc llc":"Ad Hoc",
    "ad hoc, llc":"Ad Hoc",
    "activision":"Activision Blizzard",
    "accounting firm":"Accountant",
    "accenture llp":"Accenture",
    "accenture plc":"Accenture",
    "abt":"Abt",
    "abt assoc.":"Abt",
    "abt associates":"Abt",
    "a&e networks":"A&E Networks",
    "a+e networks":"A&E Networks",
    "4 degre.es":"4degre.es",
    "4 degre.es social media agency":"4degre.es",
    "4degre.es":"4degre.es",
    "4degre.es inc":"4degre.es",
    "4degrees":"4degre.es",
    "3m":"3M",
    "3m company":"3M",
    "2u":"2U",
    "2u, inc":"2U",
    "2u, inc.":"2U",
    "20th century fox":"20th Century Fox",
    "20th century fox entertainment":"20th Century Fox",
    "20th century fox television":"20th Century Fox",
    "20th century fox tv":"20th Century Fox",
    "international business machines":"IBM",

    "Shwab":"Charles Schwab",
    "Schwab":"Charles Schwab",
    "Schwab & Co.":"Charles Schwab",

    "google.com":"Google",
    "google llc":"Google",
    "google":"Google",
    "google, inc.":"Google",
    "google inc":"Google",
    "google inc.":"Google",
    "google, inc":"Google",
    "google, inc.":"Google",
    "google, llc.":"Google",
    "google, llc":"Google",

    "uw":"University of Washington",

    "asu":"Arizona State University",

    "ut austin":"University of Texas at Austin",

    "gm":"GM",
    "general motors":"GM",
    "general motors corporation":"GM",
    "general motors co":"GM",
    "general motors co.":"GM",
    "general motors company":"GM",
    "general motors corp":"GM",
    "general motors corp.":"GM",
    "general motors corporation":"GM",
    "g.m.":"GM",

    

    "treasury department":"U.S. Department of the Treasury",
    "treasury":"U.S. Department of the Treasury",
    "us treasury":"U.S. Department of the Treasury",
    "department of the treasury":"U.S. Department of the Treasury",
    "dept of treasury":"U.S. Department of the Treasury",
    "u.s. treasury":"U.S. Department of the Treasury",
    "u.s. treasury dept":"U.S. Department of the Treasury",
    "u.s. treasury dept.":"U.S. Department of the Treasury",
    "us treasury dept":"U.S. Department of the Treasury",
    "us treasury dept.":"U.S. Department of the Treasury",
    "us treasury department":"U.S. Department of the Treasury",
    "us dept of treasury":"U.S. Department of the Treasury",
    "us dept of the treasury":"U.S. Department of the Treasury",
    "us dept. of treasury":"U.S. Department of the Treasury",
    "u.s. dept of treasury":"U.S. Department of the Treasury",
    "u.s. dept. of treasury":"U.S. Department of the Treasury",
    "u.s. department of the treasury":"U.S. Department of the Treasury",
    "u.s. dept of the treasury":"U.S. Department of the Treasury",
    "u.s. dept. of the treasury":"U.S. Department of the Treasury",
    "dept. of the treasury":"U.S. Department of the Treasury",
    "dept. treasury":"U.S. Department of the Treasury",
    "treasury dept":"U.S. Department of the Treasury",
    "treasury department":"U.S. Department of the Treasury",
    "treasury":"U.S. Department of the Treasury",
    "treasury dept.":"U.S. Department of the Treasury",
    "dept of the treasury":"U.S. Department of the Treasury",
    "dept. of the treasury":"U.S. Department of the Treasury",
    "department of the treasury":"U.S. Department of the Treasury",
    "department of treasury":"U.S. Department of the Treasury",

    "risd":"Rhode Island School of Design",

    "us dept of state":"U.S. Department of State",
    "us dept. of state":"U.S. Department of State",
    "us department of state":"U.S. Department of State",
    "u.s. department of state":"U.S. Department of State",
    "u.s. dept of state":"U.S. Department of State",
    "u.s. dept. of state":"U.S. Department of State",
    "us state dept":"U.S. Department of State",
    "us state dept.":"U.S. Department of State",
    "us state department":"U.S. Department of State",
    "u.s. state department":"U.S. Department of State",
    "u.s. state dept":"U.S. Department of State",
    "u.s. state dept.":"U.S. Department of State",
    "state department":"U.S. Department of State",
    "state dept":"U.S. Department of State",
    "state dept.":"U.S. Department of State",
    "state dept of state":"U.S. Department of State",
    "us dept. of state":"U.S. Department of State",

    "army":"U.S. Army",
    "us army":"U.S. Army",
    "u.s. army":"U.S. Army",
    "united states army":"U.S. Army",

    "csu stanislaus":"California State University Stanislaus",

    "hud":"U.S. Department of Housing and Urban Development",

    "linkedin corporation":"LinkedIn",

    "usda forest service":"U.S. Forest Service",
    "forst service":"U.S. Forest Service",
    "usfs":"U.S. Forest Service",

    "mass general hospital":"Massachusetts General Hospital",

    "wells fargo bank":"Wells Fargo",


    "uc santa cruz":"University of California Santa Cruz",

    "kpmg llp":"KPMG",

    "federal":"Federal Government",

    "us house of representatives":"U.S. House of Representatives",
    "us house of reps":"U.S. House of Representatives",
    "u.s. house of representatives":"U.S. House of Representatives",
    "house of representatives":"U.S. House of Representatives",
    "house of reps":"U.S. House of Representatives",
    "united states house of representatives":"U.S. House of Representatives",

    "senate":"U.S. Senate",
    "us senate":"U.S. Senate",
    "u.s. senate":"U.S. Senate",
    "united states senate":"U.S. Senate",

    "ca state senate":"California State Senate",
    "ca state assembly":"California State Assembly",
    "california senate":"California State Senate",
    "california assembly":"California State Assembly",

    "northwestern":"Northwestern University",

    "umkc":"University of Missouri Kansas City",

    "nyc dept of education":"New York City Department of Education",

    "verizon":"Verizon",

    "dartmouth college":"Dartmouth College",

    "umass":"University of Massachusetts",

    "GlaxoSmithKline":"GSK",
    "gsk":"GSK",

    "uc":"University of California",

    "retirednone":"Retired",

    "warner bros.":"Warner Bros",

    "deloitte consulting":"Deloitte",

    "zt systems":"ZT Systems",

    "usda":"U.S. Department of Agriculture",
    "u.s. department of agriculture":"U.S. Department of Agriculture",
    "u.s.d.a":"U.S. Department of Agriculture",

    "lausd":"Los Angeles Unified School District",
    "l.a. unified school district":"Los Angeles Unified School District",
    "la unified school district":"Los Angeles Unified School District",
    "l.a.u.s.d.":"Los Angeles Unified School District",

    "ohsu":"Oregon Health & Science University",

    "faa":"Federal Aviation Administration",
    "f.a.a.":"Federal Aviation Administration",

    "fda":"U.S. Food and Drug Administration",
    "f.d.a.":"U.S. Food and Drug Administration",
    "us fda":"U.S. Food and Drug Administration",

    "usgs":"U.S. Geological Survey",
    "us geological survey":"U.S. Geological Survey",
    "us gs":"U.S. Geological Survey",
    "u.s.g.s.":"U.S. Geological Survey",

    "doj":"U.S. Department of Justice",
    "us doj":"U.S. Department of Justice",
    "us department of justice":"U.S. Department of Justice",
    "department of justice":"U.S. Department of Justice",
    "dept. of justice":"U.S. Department of Justice",
    "u.s. dept of justice":"U.S. Department of Justice",
    "u.s. dept. of justice":"U.S. Department of Justice",
    "dept of justice":"U.S. Department of Justice",

    "ssa":"Social Security Administration",

    "the boing company":"Boeing",
    "the boeing company":"Boeing",

    "general electric":"GE",

    "Peoples Group - self-employed":"Self Employed",
    "peoples group - self-employed":"Self Employed",


    "mayo":"Mayo Clinic",

    "cisco systems":"Cisco",

    "the ohio state university":"Ohio State University",

    "fdic":"Federal Deposit Insurance Corporation",
    "f.d.i.c.":"Federal Deposit Insurance Corporation",


    "irs":"U.S. Internal Revenue Service",
    "i.r.s.":"U.S. Internal Revenue Service",
    "internal revenue service":"U.S. Internal Revenue Service",

    "u of texas":"University of Texas",
    "u of texas at austin":"University of Texas at Austin",

    "noneretired":"Retired",



    "state of ca":"State of California",
    "ca state":"State of California",

    "nys senate":"New York State Senate",

    "senate of pa":"Pennsylvania State Senate",

    "wa state":"Washington State",

    "veteran affairs":"U.S. Department of Veterans Affairs",
    "veterans affairs":"U.S. Department of Veterans Affairs",
    "veterans administration":"U.S. Department of Veterans Affairs",
    "veterans admin":"U.S. Department of Veterans Affairs",
    "veterans admin.":"U.S. Department of Veterans Affairs",
    "vet affairs":"U.S. Department of Veterans Affairs",
    "veterans affairs dept":"U.S. Department of Veterans Affairs",
    "veterans affairs department":"U.S. Department of Veterans Affairs",
    "veterans affairs dept.":"U.S. Department of Veterans Affairs",
    "us department of veterans affairs":"U.S. Department of Veterans Affairs",
    "u.s. department of veterans affairs":"U.S. Department of Veterans Affairs",
    "dept. of veterans affairs":"U.S. Department of Veterans Affairs",
    "dept of veterans affairs":"U.S. Department of Veterans Affairs",
    "us dept of veterans affairs":"U.S. Department of Veterans Affairs",
    "dept. of veterans affairs (vha)":"U.S. Department of Veterans Affairs",
    "department of veterans affairs":"U.S. Department of Veterans Affairs",
    "department of veterans afairs":"U.S. Department of Veterans Affairs",
    "department of veteran affairs":"U.S. Department of Veterans Affairs",
    "veteran's affairs admin.":"U.S. Department of Veterans Affairs",
    "va":"U.S. Department of Veterans Affairs",

    "vha":"Veterans Health Administration",


    "us dod":"U.S. Department of Defense",
    "dod":"U.S. Department of Defense",
    "dept of defense":"U.S. Department of Defense",
    "department of defense":"U.S. Department of Defense",
    "dept. of defense":"U.S. Department of Defense",
    "u.s. dept of defense":"U.S. Department of Defense",
    "u.s. dept. of defense":"U.S. Department of Defense",

    "yale":"Yale University",

    "general motors":"GM",

    "state of nj":"State of New Jersey",

    "delta":"Delta Airlines",
    "delta air lines":"Delta Airlines",

    "department of state":"U.S. Department of State",
    "state department":"U.S. Department of State",
    "dept of state":"U.S. Department of State",
    "u.s. dept of state":"U.S. Department of State",
    "u.s. dept. of state":"U.S. Department of State",
    "dept. of state":"U.S. Department of State",
    "state dept":"U.S. Department of State",
    "state dept.":"U.S. Department of State",

    "sfusd":"San Francisco Unified School District",

    "us govt":"U.S. Government",

    "us epa":"U.S. Environmental Protection Agency",
    "epa":"U.S. Environmental Protection Agency",
    "e.p.a.":"U.S. Environmental Protection Agency",

    "kaiser":"Kaiser Permanente",

    "mrs":None,
    "mrs.":None,
    "ms.":None,
    "mr.":None,

    "unm":"University of New Mexico",

    "penn state":"Pennsylvania State University",

    "bloomberg":"Bloomberg LP",

    "mgh":"Massachusetts General Hospital",

    "unlv":"University of Nevada Las Vegas",

    "state of ct":"State of Connecticut",

    "mit":"Massachusetts Institute of Technology",


    "navy":"U.S. Navy",
    "us navy":"U.S. Navy",
    "usn":"U.S. Navy",
    "united states navy":"U.S. Navy",

    "the walt disney company":"Disney",

    "nbc universal":"NBCUniversal",
    "nbc":"NBCUniversal",

    "cuny":"City University of New York",

    "nyc doe":"New York City Department of Education",
    "nycdoe":"New York City Department of Education",

    "DOE":"U.S. Department of Energy",

    "suny potsdam":"State University of New York, Potsdam",
    "suny buffalo":"State University of New York, Buffalo",
    "suny rf":"State University of New York, Research Foundation",
    "suny downstate medical center":"State University of New York, Downstate Medical Center",
    "university at albany/suny":"State University of New York, Albany",
    "suny downstate":"State University of New York, Downstate Medical Center",
    "suny at buffalo":"State University of New York, Buffalo",
    "suny research foundation":"State University of New York, Research Foundation",
    "suny old westbury":"State University of New York, Old Westbury",
    "thetis group/ suny old westbury":"State University of New York, Old Westbury",
    "suny downstate":"State University of New York, Downstate Medical Center",
    "research foundation of suny":"State University of New York, Research Foundation",
    "suny albany":"State University of New York, Albany",
    "suny cortland":"State University of New York, Cortland",
    "suny plattsburgh":"State University of New York, Plattsburgh",
    "university at albany, suny":"State University of New York, Albany",
    "college at brockport suny":"State University of New York, Brockport",
    "empire state college/suny":"State University of New York, Empire State College",
    "suny empire state college":"State University of New York, Empire State College",
    "rf suny":"State University of New York, Research Foundation",
    "suny binghamton":"State University of New York, Binghamton",
    "suny buffalo state":"State University of New York, Buffalo State",
    "suny cobleskill":"State University of New York, Cobleskill",
    "suny cortland":"State University of New York, Cortland",
    "suny delhi":"State University of New York, Delhi",
    "suny empire state":"State University of New York, Empire State College",
    "suny esf":"State University of New York, Environmental Science and Forestry",
    "suny fredonia":"State University of New York, Fredonia",
    "suny geneseo":"State University of New York, Geneseo",
    "suny suffolk":"State University of New York, Suffolk",
    "suny": "State University of New York",
    "suny-orange":"State University of New York, Orange",
    "suny at buffalo":"State University of New York, Buffalo",
    "ualbany, suny":"State University of New York, Albany",
    "suny oneonta":"State University of New York, Oneonta",
    "suny oswego":  "State University of New York, Oswego",
    "suny-buffalo":"State University of New York, Buffalo",
    "suny-buffalo state":"State University of New York, Buffalo State",
    "suny-cobleskill":"State University of New York, Cobleskill",
    "suny-cortland":"State University of New York, Cortland",
    "suny-delhi":"State University of New York, Delhi",
    "suny-esf":"State University of New York, Environmental Science and Forestry",
    "suny-fredonia":"State University of New York, Fredonia",
    "suny-geneseo":"State University of New York, Geneseo",
    "suny-orange":"State University of New York, Orange",
    "suny-oneonta":"State University of New York, Oneonta",
    "suny-oswego":"State University of New York, Oswego",
    "suny-potsdam":"State University of New York, Potsdam",
    "suny-stony brook":"State University of New York, Stony Brook",
    "suny-suffolk":"State University of New York, Suffolk",
    "suny-upstate medical university":"State University of New York, Upstate Medical University",
    "suny upstate medical university":"State University of New York, Upstate Medical University",
    "university at albany?suny":"State University of New York, Albany",
    "suny upstate medical university":"State University of New York, Upstate Medical University",
    "suny new paltz":"State University of New York, New Paltz",
    "suny upstate medical univ":"State University of New York, Upstate Medical University",
    "suny":"State University of New York",
    "suny old westbury":"State University of New York, Old Westbury",
    "university at buffalo, state university of new york":"State University of New York, Buffalo",
    "state university of new york, buffalo":"State University of New York, Buffalo",
    "suny buffalo":"State University of New York, Buffalo",
    "state university of new york at new paltz":"State University of New York, New Paltz",
    "state university of new york at buffalo":"State University of New York, Buffalo",
    "purchase college, state university of new york":"State University of New York, Purchase",
    "state university of new york, binghamton university":"State University of New York, Binghamton",
    "state university of new york, korea":"State University of New York, Korea",
    "state university of new york":"State University of New York",

    "united health group":"UnitedHealthcare",

    "rutgers the state university of new jersey":"Rutgers, The State University of New Jersey",

    "usaf":"U.S. Air Force",
    "us air force":"U.S. Air Force",
    "u.s.a.f.":"U.S. Air Force",
    "air force":"U.S. Air Force",
    "department of the air force":"U.S. Air Force",
    "united states air force":"U.S. Air Force",

    "usps":"U.S. Postal Service",
    "us postal service":"U.S. Postal Service",
    "u.s.p.s.":"U.S. Postal Service",

    "ftc":"Federal Trade Commission",
    "f.t.c.":"Federal Trade Commission",

    "salesforce.com":"Salesforce",


    "pa house of representatives":"Pennsylvania House of Representatives",
    "nh house of representatives":"New Hampshire House of Representatives",

    "university of denv":"University of Denver",
    "university of matyland":"University of Maryland",
    "unc wilmington":"University of North Carolina Wilmington",
    "univ maryland":"University of Maryland",
    "university of matyland":"University of Maryland",
    "univ of alaska":"University of Alaska",
    "univ of baltimore":"University of Baltimore",
    "univ. of arizona":"University of Arizona",
    "univ. of minnesota":"University of Minnesota",
    "univ. of mississippi":"University of Mississippi",
    "university of colo, boulder":"University of Colorado Boulder",
    "university of maryland, baltimore county":"University of Maryland Baltimore",
    "university of michigan-dearborn":"University of Michigan Dearborn",

    "bcg":"Boston Consulting Group",

    "nyu school of medicine":"New York University, School of Medicine",
    "nyu/steinhardt":"New York University, Steinhardt",
    "nyu abu dhabi":"New York University, Abu Dhabi",
    "nyu tandon school of engineering": "New York University, Tandon School of Engineering",

    "nvidia":"Nvidia",

    "dell, inc":"Dell",
    "dell inc":"Dell",
    "dell inc.":"Dell",
    "dell, inc.":"Dell",
    "dell technologies":'Dell',

    "usnrc":"U.S. Nuclear Regulatory Commission",

    "dr.":"Physician",

    "unc chapel hill":"University of North Carolina Chapel Hill",


    "uspto":"U.S. Patent and Trademark Office",

    "ucsd":"University of California San Diego",
    "u.c.s.d.":"University of California San Diego",
    "university of california, san diego":"University of California San Diego",
    "uc san diego":"University of California San Diego",
    "u.c. san diego":"University of California San Diego",
    "uc sandiego":"University of California San Diego",
    "ucsf":"University of California San Francisco",
    "university of california, san fransisco":"University of California San Francisco",
    "u.c.s.f.":"University of California San Francisco",
    "ucla":"University of California Los Angeles",
    "university of california, los angeles":"University of California Los Angeles",
    "u.c.l.a.":"University of California Los Angeles",
    "uc berkeley":"University of California Berkeley",
    "university of california, berkeley":"University of California Berkeley",
    "u.c. berkeley":"University of California Berkeley",
    "uc davis":"University of California Davis",
    "u.c. davis":"University of California Davis",
    "university of california, davis":"University of California Davis",
    "uc irvine":"University of California Irvine",
    "u.c. irvine":"University of California Irvine",
    "university of california, irvine":"University of California Irvine",
    "uc riverside":"University of California Riverside",
    "u.c. riverside":"University of California Riverside",
    "university of california, riverside":"University of California Riverside",
    "uc san diego":"University of California San Diego",
    "u.c. san diego":"University of California San Diego",
    "university of california, san diego":"University of California San Diego",
    "uc santa barbara":"University of California Santa Barbara",
    "u.c. santa barbara":"University of California Santa Barbara",
    "university of california, santa barbara":"University of California Santa Barbara",
    "uc santa cruz":"University of California Santa Cruz",
    "university of california, santa cruz":"University of California Santa Cruz",
    "u.c. santa cruz":"University of California Santa Cruz",
    "usc":"University of Southern California",
    "u.s.c.":"University of Southern California",

    "u s coast guard":"U.S. Coast Gaurd",
    "us coast guard":"U.S. Coast Gaurd",
    "u.s. coast guard":"U.S. Coast Gaurd",
    "coast guard":"U.S. Coast Guard",

    "chicago board of ed.":"Chicago Board of Education",
    "chicago board of education":"Chicago Board of Education",
   "chicago board of ed":"Chicago Board of Education",

    "nyc schools":"New York City Public Schools",
    "nyc public schools":"New York City Public Schools",
    "nyc publix schools":"New York City Public Schools",
    "nyc school":"New York City Public Schools",
    "nyc schools":"New York City Public Schools",
    "new york city public school":"New York City Public Schools",

    "h.p.":"HP",
    "hp inc.":"HP",

    "emory":'Emory University',

    "microsoft corporation":"Microsoft",

    "smithsonian":"Smithsonian Institution",

    "city and county of homolulu":"City and County of Honolulu",

    "university of california, berkeley":"University of California Berkeley",

    "a":None,#though should have already cought i think

    'uw-madison':"University of Wisconsin Madison",

    "fau":"Florida Atlantic University",

    "state of fl":"State of Florida",

    "no":None,

    "intel corporation":"Intel",

    "vz":"Verizon",

    "usaid":"USAID",
    "nih":"NIH",

    "parents":"Parents",

    "commonwealth of pa":"Commonwealth of Pennsylvania",
    "commonwealth of massachusetts":"Commonwealth of Massachusetts",

    "csu chico":"California State University Chico",

    "epa":"U.S. Environmental Protection Agency",
    "us epa":"U.S. Environmental Protection Agency",
    "us environmental protection agency":"U.S. Environmental Protection Agency",
    "u.s. epa":"U.S. Environmental Protection Agency",
    "u.s. e.p.a.":"U.S. Environmental Protection Agency",

    "the home depot":"Home Depot",

    "rutgers":"Rutgers University",

    "upmc":"University of Pittsburgh Medical Center",
    "u.p.m.c.":"University of Pittsburgh Medical Center",

    "radiology associates":"Radioogy Associates",

    "stanford":"Stanford University",

    "dartmouth":"Dartmouth College",
    "emerson":"Emerson College",

    "the gap, inc.":"Gap Inc.",
    "gap inc":"Gap Inc.",

    "skadden":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden arps et al":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden, arps, slate, meagher & flom":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden arps slate meagher & flom llp":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden, arps, slate, meagher & flom llp":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden, arps":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden arps":"Skadden, Arps, Slate, Meagher & Flom LLP",
    "skadden, arps et al":"Skadden, Arps, Slate, Meagher & Flom LLP",

    "petsmart":"PetSmart",

    "{{employer}}":None,
    "%%employer%%":None,
    "employer":None,
    "no":None,
    "default":None,
    "blank":None,

    "nlrb":	"National Labor Relations Board",
    "national labor relations board":	"National Labor Relations Board",
    "national labor relations board (nlrb)":	"National Labor Relations Board",
    "n.l.r.b.": "National Labor Relations Board",

    "chrysler":"FCA",
    "fiat":"FCA",
    "fca (fiat chrysler automobiles":"FCA",
    "fca":"FCA",
    "fiat chrysler":"FCA",
    "fiat chrysler automobiles":"FCA",
    "chrysler llc":"FCA",
    "chryslerllc":"FCA",
    "chrysler llc":"FCA",
    "fiat chrysler automobile":"FCA",
    "chrysler llc":"FCA",
    "fiat chrysler automobiles":"FCA",
    "fiat chrysler":"FCA",
    "fiat auto":"FCA",
    "fiat chrysler auto":"FCA",
    "fca llc":"FCA",
    "fca us llc":"FCA",

    "Walgreen Co.":"Walgreens",

    "n/a.":"Not Employed",
    "i am not working":"Not Employed",

    "na.":"Not Employed",
    "n.a.":"Not Employed",

    

}

common_occupation_titles = {
    "selk":"Self Employed",
    "none":"Not Employed",
    "n/a.":"Not Employed",
    "na.":"Not Employed",
    "n.a.":"Not Employed",
    "i am not working":"Not Employed",
    "unemployed":"Not Employed",
    "nothing":"Not Employed",
    "self":"Self Employed",
    "own business":"Self Employed",
    "own":"Self Employed",
    "myself":"Self Employed",
    "me":"Self Employed",
    "rn":"Registered Nurse",
    "default":None,
    "blank":None,
    "your mom":None,
    "n\a":"Not Employed",
    "n/a":"Not Employed",
    "na":"Not Employed",
    "consulting":"Consultant",
    "consultant":"Consultant",
    "consultant/self":"Consultant",
    "consultant/self employed":"Consultant",
    "consultant/self-employed":"Consultant",
    "- select -":None,
     "xx":None,
    "xxx":None,
    "xxxx":None,
    "xxxxx":None,
    "xxxxxxx":None,
    "xxxxxxxxx":None,
    "xyz":None,
    "can't say":None,
    "@properties":None,
    "a job":None,
    "me":"Self Employed",
    "occupation":None,
    "amounts=5,10,25,50,100,150,250":None,
    "asd":None,
    "asdf":None,
    "work":None,
    "self.":"Self Employed",
    ".self":"Self Employed",
    "aelf":"Self Employed",
    "self":"Self Employed",
    "self employed":"Self Employed",
    "self-employed":"Self Employed",
    "retired":"Retired",
    "none":"Not Employed",
    "not employed":"Not Employed",
    "not-employed":"Not Employed",
    "ceo":"CEO",
    "cto":"CTO",
    "cfo":"CFO",
    "exec director":"Executive Director",
    "a bank":"Banking",
    "cpa":"Accountant",
    "lawyer":"Attorney",
    "attorney":"Attorney",
    "law":"Attorney",
    "lawyer/consultant":"Attorney",
    "attorney/consultant":"Attorney",
    "attoeney":"Attorney",
    "bookkeeper":"Accountant",
    "bookkeeping":"Accountant",
    "admin asst":"Administrative Assistant",
    "admin":"Administrator",
    "aprn":"Advanced Practitioner Nurse",
    "estimator":"Appraiser",
    "atty":"Attorney",
    "attorney at law":"Attorney",
    "ceo":"CEO",
    "cna":"Certified Nurses Assistant",
    "chro":"Chief Human Resources Officer",
    "cio":"Chief Information Officer",
    "cmo":"Chief Marketing Officer",
    "coo":"Chief Operations Officer",
    "cto":"Chief Technology Officer",
    "copyeditor":"Copy Editor",
    "csr":"Customer Service Representative",
    "customer service rep":"Customer Service Representative",
    "dba":"Database Administrator",
    "devops engineer":"Developer Operations Engineer",
    "writer/editor":"Editor",
    "education":"Educator",
    "evp":"Executive Vice President",
    "gm":"General Manager",
    "mom":"Homemaker",
    "medical doctor":"Physician",
    "retired rn":"Retired",
    "%%occupation%%":None,
    "{{occupation}}":None,
    "occupation":None,
    "ret":"Retired",
    "no":None,
    "housewife":"Homemaker",
    "mother":"Homemaker",
    "stay at home mom":"Homemaker",
    "hr":"Human Resources",
    "hr consultant":"Human Resources Consultant",
    "hr director":"Human Resources Director",
    "hr specialist":"Human Resources Specialist",
    "it":"Information Technology",
    "it specialist":"Information Technology",
    "it analyst":"Information Technology Analyst",
    "it architect":"Information Technology Architect",
    "it consultant":"Information Technology Consultant",
    "it director":"Information Technology Director",
    "it engineer":"Information Technology Engineer",
    "it manager":"Information Technology Manager",
    "it professional":"Information Technology Professional",
    "it project manager":"Information Technology Project Manager",
    "it security":"Information Technology Security",
    "it support":"Information Technology Support",
    "lawyer/housewife":"Lawyer",
    "mgr":"Manager",
    "marketer":"Marketing",
    "mft":"Marriage and Family Therapist",
    "lmt":"Massage Therapist",
    "n/a":"None",
    "Physican":"Physician",
    "na":"None",
    "director of it":"Director of Information Technology",
    "non profit":"Nonprofit",
    "non-profit":"Nonprofit",
    "nonprofit consultant":"Nonprofit Consultant",
    "none":"Not Employed",
    "not-employed":"Not Employed",
    "unemployed":"Not Employed",
    "not emplyed":"Not Employed",
    "office mgr":"Office Manager",
    "pca":"Personal Care Assistant",
    "md":"Physician",
    "doctor":"Physician",
    "m.d.":"Physician",
    "pa":"Physicians Assistant",
    "postdoc":"Post Doctorate Student",
    "program mgr":"Program Manager",
    "programmer/analyst":"Programmer",
    "project mgr":"Project Manager",
    "qa analyst":"Qualatiy Assurance Analyst",
    "qa":"Quality Assurance",
    "qa engineer":"Quality Assurance Engineer",
    "rn":"Registered Nurse",
    "r.n.":"Registered Nurse",
    "retired teacher":"Retired",
    "retiree":"Retired",
    "not employed/retired":"Retired",
    "economist (retired)":"Retired",
    "salesman":"Sales",
    "sales rep":"Sales Representative",
    "self":"Self Employed",
    "self-employed":"Self Employed",
    "sr manager":"Senior Manager",
    "svp":"Senior Vice President",
    "computer programmer":"Software Developer",
    "sw engineer":"Software Engineer",
    "system engineer":"Systems Engineer",
    "public school teacher":"Teacher",
    "vp":"Vice President",
    "vp marketing":"Vice President Marketing",
    "vp sales":"Vice President Sales",
    "writer/producer":"Writer"
    
}



#SKIP TOP EMPLOYERS
skip_top_employers = ["Not Employed",
"Google",
"Amazon",
"Microsoft",
"Harvard University",
"Facebook",
"State of California",
"IBM",
"Stanford University",
"Kaiser Permanente",
"University of California",
"University of Washington",
"Wells Fargo",
"Columbia University",
"University of Michigan",
"Oracle",
"MIT",
"Salesforce",
"New York University",
"AT&T",
"UIC",
"Federal Government",
"Dartmouth College",
"Deloitte",
"Boston University",
"Boeing",
"Accenture",
"University of Florida",
"Rutgers University",
"University of Chicago",
"NYU",
"Northwestern University",
"Disney",
"Verizon",
"Bank of America",
"University of Pennsylvania",
"Yale University",
"University of Colorado",
"Northrop Grumman",
"Hospital",
"American Airlines",
"Lockheed Martin",
"Raytheon",
"Ms.",
"Indiana University",
"University of Kansas",
"Walmart",
"Comcast",
"Student",
"United Airlines",
"Temple University School of Medicine",
"Capital One",
"University of Minnesota",
"Target",
"Apple Inc.",
"Cornell University",
"Netflix",
"University",
"Intel",
"Tufts University",
"University of Iowa",
"PwC",
"University of Miami",
"George Mason University",
"Federal Government",
"City of New York",
"University of Maryland",
"Starbucks",
"Uber",
"State of Iowa",
"Johns Hopkins University",
"Twitter",
"Apple, Inc.",
"Emory University",
"State of Florida",
"University of Illinois",
"NASA",
"Genentech",
"Cisco",
"Arizona State University",
"Adobe",
"State of Montana",
"Brown University",
"EY",
"Duke University",
"Montana State University",
"Optum",
"Leidos",
"LinkedIn",
"University of Montana",
"Georgetown University",
"CBS",
"Social Security Administration",
"Pfizer",
"Home Depot",
"FTI Consulting",
"Weikart center",
"HCA",
"Princeton University",
"University of Southern California",
"University of Utah",
"American Express",
"Novartis",
"Thomson Reuters",
"UPS",
"Booz Allen Hamilton",
"University of Pittsburgh",
"Northeastern University",
"Coldwell Banker",
"Nike",
"KPMG",
"Siemens",
"State of Colorado",
"School",
"University of Arizona",
"Stripe",
"AECOM",
"City of Los Angeles",
"Walgreens",
"Kroger",
"University of Virginia",
"MetLife",
"American University",
"State of Maine",
"USG",
"Boston College",
"Autodesk",
"Airbnb",
"NIH",
"Lyft",
"WilmerHale",
"Iowa State University",
"TPMG",
"NBCUniversal",
"CCSD",
"Jones Day",
"Oregon State University",
"U.S. Government",
"BAE Systems",
"VMware",
"Sutter Health",
"Liberty Mutual",
"Epic",
"SAP",
"George Washington University",
"Commonwealth of Massachusetts",
"Cooley LLP",
"NIH",
"Parents",
"Los Angeles Unified School District",
"Becker College",
"U.S. Department of Veterans Affairs",
"Goodwill",
"Yale University",
"Portland Public Schools",
"FIS",
"Square",
"Nonprofit",
"Penguin Random House",
"Honeywell",
"Bates College",
"City of Seattle",
"Medtronic",
"AIG",
"Florida State University",
"Sidley Austin LLP",
"Michigan State University",
"Dell",
"The Nature Conservancy",
"Law firm",
"Temple University",
"GE",
"Baylor College Of Medicine",
"Spotify",
"CVS",
"ADP",
"Brandeis University",
"Kansas State University",
"Drake University",
"Aetna",
"Staples",
"Dropbox",
"Costco",
"T-Mobile",
"University of Missouri",
"Cigna",
"Mayo Clinic",
"Aon",
"Anthem",
"USAA",
"YMCA",
"Enloe Medical Center",
"National Park Service",
"Engineer",
"Johns Hopkins",
"PG&E",
"Drexel University",
"State of Kansas",
"Jacobs",
"Bloomberg LP",
"Merck",
"University of Denver",
"Viacom",
"Various",
"Loudoun County Public Schools",
"Intuit",
"Humana",
"University of Oregon",
"Baylor College of Medicine",
"State of Oregon",
"State",
"New York State",
"Gartner",
"Compass",
"Bank",
"Providence",
"USAID",
"Freddie Mac",
"Santa Clara County",
"University of Texas at Austin",
"DePaul University",
"Florida International University",
"Carnegie Mellon University",
"University of New Mexico",
"University of New Hampshire",
"MCPS",
"Denver Public Schools",
"HPE",
"Cleveland Clinic",
"Gensler",
"Portland State University",
"University of South Florida",
"Johnson & Johnson",
"CBRE",
"Des Moines Public Schools",
"Washington University",
"TD Bank",
"United Methodist Church",
"Banner Health",
"Wayfair",
"City College of San Francisco",
"Ohio State University",
"Bob's Copy Shop",
"City and County of San Francisco",
"Sony",
"U.S. Navy",
"Virginia Tech",
"Dignity Health",
"Patterson Belknap Webb & Tyler",
"King County",
"University of Wisconsin",
"Nordstrom",
"McKinsey & Company",
"Morgan Stanley",
"Workday",
"Kirkland & Ellis LLP",
"Penn State University",
"Chevron",
"Purdue University",
"Centene",
"Southwest Airlines",
"San Jose State University",
"GDIT",
"U.S. Department of State",
"Billings Clinic",
"Colorado State University",
"General Dynamics",
"Butte College",
"GM",
"University of Delaware",
"State Farm",
"JLL",
"Covington & Burling LLP",
"US Bank",
"University of Texas",
"3M",
"MaineGeneral Medical Center",
"Prudential",
"UnitedHealthcare",
"Maine Medical Center",
"Transamerica",
"Georgia Tech",
"Safeway",
"Seton Hall University",
"Abbott",
"New York State DOT Region 1",
"Chicago Public Schools",
"Vanderbilt University",
"Alameda County",
"Hendrickson Construction Inc",
"NYC",
"Sierra Club",
"ASPCA",
"City University of New York",
"University of Rochester",
"University of Kentucky",
"University of Notre Dame",
"Entertainment Partners",
"Montclair State University",
"Indeed",
"NCQA",
"Cerner",
"Teacher",
"State of Alaska",
"Macmillan",
"Boston Children's Hospital",
"Portland Public Schools",
"University of Hawaii",
"Mayer Brown LLP",
"City of Chicago",
"CDC",
"Tesla",
"SaneBox",
"Federal Public Defender",
"CVS Health",
"Morgan Lewis",
"McKesson",
"Arnold & Porter",
"SAIC",
"Edelman",
"State of Washington",
"Mednax",
"Teach For America",
"State of Illinois",
"Fannie Mae",
"Many Mansions",
"Massachusetts Institute of Technology",
"University of Massachusetts",
"Visa",
"PIMG",
"Ernst & Young",
"Nationwide",
"CenturyLink",
"APS",
"California State University",
"Citigroup",
"Independent Contractor",
"Smithsonian Institution",
"FedEx",
"Zendesk",
"Jackson family fine wines",
"Green Cab of Madison",
"Westat",
"Fordham University",
"Citi",
"Whole Foods Market",
"Syracuse University",
"Atlassian",
"Allstate",
"Akamai Technologies",
"Sprint",
"Morrison & Foerster LLP",
"Charles Schwab",
"Mercer",
"Seattle Public Schools",
"Owner",
"HBO",
"Insight Global",
"Harvard Law School",
"ViacomCBS",
"Abbvie",
"Travelers",
"ExxonMobil",
"Library of Congress",
"Goodwin Procter LLP",
"University of Georgia",
"Keller Williams",
"Independent",
"Outlines Menswear",
"Mastercard",
"PayPal",
"Pinterest",
"Disabled",
"Ropes & Gray LLP",
"NYS",
"Northwell Health",
"Willis Towers Watson",
"Slack",
"Holland & Hart LLP",
"Green America",
"H&R Block",
"Fairfax County",
"Greenberg Traurig",
"BNY Mellon",
"Bain & Company",
"Lewis Katz School of Medicine at Temple University",
"Warner Bros",
"Broadcom",
"Slalom",
"Winsupply Pioneer Valley",
"Dechert LLP",
"McKinsey",
"School District",
"Nvidia",
"Quest Diagnostics",
"Mental Health Association in NJ",
"Red Hat",
"Sanofi",
"Amgen",
"City of Boston",
"United Nations",
"Applied Materials",
"Edward Jones",
"Epic Systems",
"Nokia",
"NetApp",
"ActBlue",
"Physician",
"Evans Stout",
"State of Michigan",
"Asana",
"State of Minnesota",
"Mozilla",
"Pixar",
"Public Health Institute",
"Perspecta",
"Daniel D Casale Customs Broker, Inc.",
"CSRA",
"The Permanente Medical Group",
"Modesto City Schools",
"EMC",
"Wayne State University",
"NOAA",
"Pace University",
"Forensic Botany LLC",
"FIU",
"Hamilton College",
"University of Kansas Medical Center",
"TPA",
"American Red Cross",
"Ford Motor Company",
"Thermo Fisher Scientific",
"University of San Francisco",
"Adecco",
"Santa Clara University",
"Latham & Watkins",
"Qualcomm",
"City of San Francisco",
"IQVIA",
"Tech",
"Manager",
"Chase",
"Boston Public Schools",
"Splunk",
"Brigham and Women's Hospital",
"HubSpot",
"Allergan",
"The Juilliard School",
"Civis Analytics",
"GEICO",
"World Bank",
"Atlantic Health System",
"San Francisco State University",
"DCPS",
"U.S. House of Representatives",
"Sunflower Community Action",
"HP",
"Wood",
"Charter Communications",
"Wichita State University",
"Etsy",
"writer",
"Harvard Medical School",
"Keller Williams Realty",
"GitHub",
"Tulane University",
"Case Western Reserve University",
"CACI",
"Arcadia University",
"State of Texas",
"University of Tennessee",
"Publix",
"Twilio",
"university",
"Federal Trade Commission",
"Gibson Dunn",
"Colby College",
"Texas Instruments",
"Stony Brook University",
"FEMA",
"Berkeley Unified School District",
"UBS",
"Biogen",
"Kirkland & Ellis",
"Beth Israel Deaconess Medical Center",
"Howard University",
"County",
"University of Illinois at Chicago",
"National Institutes of Health",
"County of Los Angeles",
"SpaceX",
"Alaska Airlines",
"UM",
"Fiserv",
"Hulu",
"Paul Hastings LLP",
"University of Wisconsin-Madison",
"Public School",
"Progressive",
"Barnes & Noble",
"Credit Suisse",
"Children's Hospital of Philadelphia",
"Weill Cornell Medicine",
"BioMarin Pharmaceutical",
"Amazon Web Services",
"Boston Consulting Group",
"Montefiore Medical Center",
"U.S. Department of Justice",
"CSU",
"College of Southern Nevada",
"Employed",
"City and County of Denver",
"IHSS",
"Build.com",
"Dolby Laboratories",
"Rush University Medical Center",
"PepsiCo",
"Ingberdental",
"Kent State University",
"Cushman & Wakefield",
"Aramark",
"ServiceNow",
"Meredith Corporation",
"Expedia",
"University of Massachusetts Amherst",
"Urban Institute",
"Zillow Group",
"Northern Arizona University",
"Bozeman Health",
"State of Nevada",
"ATT",
"Strategy PR",
"DLA Piper",
"ServiceTitan"]

skip_top_employers_set = set(skip_top_employers)




#ADDRESSES
#b is boundary so words can be start or end of string
address_replacements = {
    r'\bAPT\b': 'Apartment',
    r'\bSTE\b': 'Suite',
    r'\bSTE\.\b': 'Suite',
    r'\bFLOOR\b': 'Floor',
    r'\bROOM\b': 'Room',
    r'\bRM\.\b': 'Room',
    r'\bRM\b': 'Room',
    r'\bUNIT\b': 'Unit',
    r'\bUT\.\b': 'Unit',
    r'\bAPARTMENT\b': 'Apartment',
    r'\bAPMNT\b': 'Apartment',
    r'\bAPMT\b': 'Apartment',
    r'\bSUITE\b': 'Suite',
    r'\bDPT\b': 'Department',
    r'\bDEPARTMENT\b': 'Department',
    r'\bNBR\b': 'Number',
    r'\bNMBR\b': 'Number',
    r'\bNUMBER\b': 'Number',
    r'\ST\b': 'Street',
    r'\ST.\b': 'Street',
    r'\bNUMBER\b': 'Number',
}


#EMAILS


top_domains = ["yahoo.com","aim.com", "aol.com","ski.com", "att.net", "juno.com", "frontier.com", "frontiernet.net", "bellsouth.net", "btinternet.com", "charter.net", "comcast.net", "cox.net", "earthlink.net", "gmail.com", "google.com", "googlemail.com", "icloud.com","qwest.net", "mac.com", "me.com", "msn.com", "optonline.net", "optusnet.com.au","cs.com", "qq.com", "q.com","rocketmail.com", "rogers.com", "sbcglobal.net", "shaw.ca", "sky.com", "sympatico.ca", "telus.net", "verizon.net", "web.de", "xtra.co.nz", "ymail.com", "yahoo.com", "hotmail.com", "hotmail.co.uk", "hotmail.fr", "yahoo.fr", "wanadoo.fr", "orange.fr", "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr", "gmx.de", "yandex.ru", "libero.it", "outlook.com", "uol.com.br", "bol.com.br", "mail.ru", "hotmail.it", "sfr.fr", "live.fr","live.co.uk", "yahoo.es", "dl.com","hotmail.fr","ig.com.br", "live.nl","nc.rr.com","countrywide.com","email.arizona.edu","netzero.net","rochester.rr.com","du.edu","colorado.edu","bhfs.com","dpsk12.org","ecentral.com","centurylink.net","mindspring.com","law.du.edu","hollandhart.com", "bigpond.com", "terra.com.br", "yahoo.it", "neuf.fr", "yahoo.de", "alice.it", "laposte.net", "facebook.com", "yahoo.in", "hotmail.es", "yahoo.ca", "yahoo.com.au", "rambler.ru", "hotmail.de","geocities.com","blackplanet.com","compuserve.com", "tiscali.it", "yahoo.co.jp", "freenet.de", "t-online.de", "aliceadsl.fr", "virgilio.it", "home.nl", "telenet.be", "yahoo.com.ar", "tiscali.co.uk", "yahoo.com.mx", "voila.fr", "gmx.net", "mail.com", "planet.nl", "tin.it", "live.it", "ntlworld.com", "arcor.de", "yahoo.co.id", "frontiernet.net", "hetnet.nl", "live.com.au", "yahoo.com.sg", "zonnet.nl", "club-internet.fr", "blueyonder.co.uk", "bluewin.ch", "skynet.be", "windstream.net", "centurytel.net", "chello.nl", "live.ca", "bigpond.net.au"]
bad_phrases = ["fake@hotmail.com","politicalemail","example.com","no___reply","no__reply","no_reply","noreply","donotemail","fake@fake.com","fake.com","iwontreadyourshit@gmail.com","donotemailme@noname.com","smith@none.net","donotemail", "donotcontact", "fakeemail", "fake.com","123456","contoso.com", "noemail", "example.net", "example.org", "mailinator.com","none@none.com","none@noemail.com","none@gmail.com","none@email.com","none@no.com","none.com","none.co","no.com","no.co","none.com","noone.com"]
suppress_domains_contains = ["mothershipstrategies.com","mainedems.org","endcitizensunited.org","hidebox","westrb","ovaki","congressional","congress","senate","nottrack","norack","mailinator","congress","senate","governor","steveodorisio.com","crestedbuttenews.com","fox31.com","denvernewshd","aspendailynews","morgancarroll","leedriscoll.com","kazba.com","kazba.co","jenaforcolorado.com","johnwalshforcolorado.com","aschkinasi.com","kathleenformontana.com","kusterforcongress.com","audreyforcongress.com","www.susieleeforcongress.com","hiral4congress.com","getthegreendeal.com","fortgangforassembly.com","tomohalleran.com","hiralforcongress.com","debbieforcongress.com","floridadems.org","cindyaxneforcongress.com","lindseysimmons.com","bollierforkansas.com","wilmotcollins.com","teresaforall.com","ginaortizjones.com","jaredgoldenforcongress.com","yesonnationalpopularvote.com","droptheacalawsuit.com","montanademocrats.org","stephendaniel.com","ritahart.com","votebymailpetition.com","teamsterpowerslate.com","griswoldataorcolorado.org ","xavierforvirginia.com","mivecinotogether.com","boebertmustgo.com","mindsovershootings.com","stewartnavarre.com","ridemocrats.org","denverdems.net","jasonminnicozzi.com","tedescoforcongress.com","ballardataormontana.com","normoyleforcongress.com","matsuiforcongress.com","evertonblair.com","davidpeterson.us","electkatiedean.com","kenrussellforflorida.com","adamforcolorado.com","drkathleenharder.com","marlinga4congress.com","cisconv.co","sarahmorgenthau.com","electblackwomenpac.com","sarahkleehoodny.com","sandeepfortexas.com","dcpa.org","healthnetco.com","educationnorthwest.org","denverwater.org","kiowacountyindependent.com","shermanhoward.com","jacksonkelly.com","boulderchamber.com","burgsimpson.com","irelandstapleton.com","googlegroups.com","re-law.com","broncos.nfl.net","mountainstatestoyota.com","rockymountainnews.com","westword.com","denverpost.com","dp.com"]
misspelled_tlds = {
    ".comf":".com",
    ".ocm":".com",
    ".con":".com",
    ".come":".com",
    ".cmo":".com",
    ".copm": ".com",
    ".xom": ".com",
    ".com,": ".com",
    ".vom": ".com",
    ".comn": ".com",
    ".co,": ".com",
    ".comj": ".com",
    ".coim": ".com",
    ".cpm": ".com",
    ".colm": ".com",
    ".conm": ".com",
    ".coom": ".com",
    ".nett":".net",
    ".comm":".com",
    ".ccom":".com",
    ".comd":".com",
    "comjr":".com",
    ".ner":".net",
    ".eud":".edu",
    ".eduu":".edu",
    ".eedu":".edu"
    #.cm is an actual tld...
}
misspelled_domains = {
    "aol.cm":"aol.com",
    "a0l.com":"aol.com",
    "aol.co":"aol.com",

    "att.ne":"att.net",
    "at.net":"att.net",

    "hotmial.com":"hotmail.com",

    #only valid gmail is gmail.com and googlemail.com
    "gmail.org":"gmail.com",
    "gmail.cm":"gmail.com",
    "gnaik.com":"gnaik.com",
    "gtmail.com":"gmail.com",
    "gmil.com":"gmail.com",
    "gmaim.com":"gmail.com",
    "gmai.com":"gmail.com",
    "gnail.com":"gmail.com",
    "gail.com":"gmail.com",
    "gmail.co":"gmail.com",
    "gmal.com":"gmail.com",
    "gmial.com":"gmail.com",
    "gmia.com":"gmail.com",
    "gmal.cm":"gmail.com",
    "g-mail.com":"gmail.com",
    "gmaill.com":"gmail.com",
    "gmail.co.uk":"gmail.com",
    "googlemail.co.uk":"gmail.com",
    "gmail.com.au":"gmail.com",
    "gmail.ca":"gmail.com",
    "googlemaile.com":"gmail.com",
    "googlmail.com":"gmail.com",
    "gmail.fr":"gmail.com",
    "gmail.com.mx":"gmail.com",
    "gmail.nl":"gmail.com",
    "googlmail.com":"gmail.com",
    "gmaio.com":"gmail.com",
    "gmainl.com":"gmail.com",
    "gmil.com":"gmail.com",
    "agmail.com":"gmail.com",
    "gmaul.com":"gmail.com",
    "gmaol.com":"gmail.com",
    "gmailm.com":"gmail.com",
    "gnsil.com":"gmail.com",
    "gmlail.com":"gmail.com",

    "earthlin.net":"earthlink.net",
    "earthlink.nt":"earthlink.net",
    "rthlink.net":"earthlink.net",
    "eartthlink.net":"earthlink.net",
    "esrthlink.net":"earthlink.net",
    "eaerthlink.net":"earthlink.net",
    "earhlink.net":"earthlink.net",
    "esearthlink.net":"earthlink.net",
    "eaearthlink.net":"earthlink.net",

    "optonlie.net":"optonline.net",
    "opotonline.net":"optonline.net",
    "optonlie.net":"optonline.net",


    "fromtiernet.net":"frontiernet.net",

    "junov.com":"juno.com",

    #opotonline optonline optonlie

    "mail.arizona.edu":"email.arizona.edu",
    "eemail.arizona.edu":"email.arizona.edu",

    "sbcgobal.net":"sbcglobal.net",


    "winstream.net":"windstream.net",

    "mdn.com":"msn.com",
    "nsm.com":"msn.com",
    "msn.cm":"msn.com",
    "mam.com":"msn.com",
    "mwm.com":"msn.com",
    "nam.com":"msn.com",
    "msnn.com":"msn.com",

    "icoud.com":"icloud.com",
    "icound.com":"icloud.com",

    "cmcast.net":"comcast.net",
    "comcst.net":"comcast.net",
    "cmcst.net":"comcast.net",
    "camcast.net":"comcast.net",
    "comcsst.net":"comcast.net",
    "cmcast.net":"comcast.net",
    "cimcast.net":"comcast.net",
    "concast.net":"comcast.net",
    "comcast.nt":"comcast.net",
    "comcast.nrt":"comcast.net",
    "comcast.ne":"comcast.net",
    "comcast.et":"comcast.net",
    "comcast.met":"comcast.net",
    "cpmvast.net":"comcast.net",

    "live.net":"live.net",
    "liv.net":"live.net",
    "live.nt":"live.net",

    "iclod.com":"icloud.com",
    "iclound.com":"icloud.com",

    "outloook.com":"outlook.com",
    "otlook.com":"outlook.com",
    "outlook.co":"outlook.com",
    "outlok.com":"outlook.com",
    "outllok.com":"outlook.com",

    "cx.net":"cox.net",
    "cox.nt":"cox.net",
    "cit.net":"cox.net",
    "xox.net":"cox.net",

    "verzon.net":"verizon.net",
    "vrizon.net":"verizon.net",
    "verizn.net":"verizon.net",
    "verizon.nt":"verizon.net",
    "verizon.ne":"verizon.net",
    "vrrizon.net":"verizon.net",
    "verozon.net":"verizon.net",
    "verizen.net":"verizon.net",

    "hotmail.cm":"hotmail.com",
    "hoymail.com":"hotmail.com",
    "homail.com":"hotmail.com",
    "hotmai.com":"hotmail.com",
    "hotmail.co":"hotmail.com",
    "hotmal.com":"hotmail.com",
    "hotmil.com":"hotmail.com",
    "hotmain.com":"hotmail.com",

    "hoymail.fr":"hotmail.fr",
    "homail.fr":"hotmail.fr",
    "hotmai.fr":"hotmail.fr",
    "hotmal.fr":"hotmail.fr",
    "hotmil.fr":"hotmail.fr",
    "hotmain.fr":"hotmail.fr",

    "mscd.edu":"msudenver.edu",

    "hotmial.co.uk":"hotmail.co.uk",
    "hotmall.co.uk":"hotmail.co.uk",
    "hotmaiil.co.uk":"hotmail.co.uk",

    "ymail.com":"yahoo.com",
    "yahoo.cm":"yahoo.com",
    "yaoo.cm":"yahoo.com",
    "yaho.com":"yahoo.com",
    "yaoo.com":"yahoo.com",
    "yahooo.com":"yahoo.com",
    "yhaoo.com":"yahoo.com",
    "ayhoo.com":"yahoo.com",
    "dyahoo.com":"yahoo.com",
    "ahoo.com":"yahoo.com",
    "yhoo.com":"yahoo.com",
    "yahool.com":"yahoo.com",
    "yhoo.com":"yahoo.com",
    "yahoomail.com":"yahoo.com",
    "tyahoo.com":"yahoo.com",
    "yahool.com":"yahoo.com",
    "yahoo.net":"yahoo.com",
    "yshoo.com":"yahoo.com",
    "yaoo.cm":"yahoo.com",
    "yaoo.com":"yahoo.com",
    "yyyahoo.com":"yahoo.com",
    "yyahoo.com":"yahoo.com",
    "yanoo.com":"yahoo.com",
    "yaboo.com":"yahoo.com",
    "yaho":"yahoo.com"

}


banned_domains_to_block = [
    "crankymonkey.info",
    "mailinator.com",
    "temp-mail.org",
    "10minutemail.com",
    "mailsac.com",
    "emailondeck.com",
    "www.emailondeck.com",
    "yopmail.com",
    "quik.email",
    "phantom-mail.io",
    "tempmailz.net",
    "mailfast.pro",
    "gmailnator.com",
    "adguard.com",
    "mailcurity.com",
    "pelagius.net",
    "guerrillamail.net",
    "guerillamail.com",
    "cs.email",
    "eml.monster.com",
    "quickemailverification.com",
    "clean.email",
    "luckymail.com",
    "throwawaymail.com",
    "temp-mail.org",
    "mailmodo.com",
    "luxusmail.org",
    "gufum.com",
    "tempail.com",
    "maildrop.cc",
    "getnada.com",
    "inboxes.com",
    "internxt.com",
    "maildrop.cc",
    "fakeinbox.com",
    "getnada.com",
    "spamgourmet.com",
    "mailnesia.com",
    "trash-mail.com",
    "mytrashmail.com",
    "mintemail.com",
    "deadaddress.com",
    "spoofmail.de",
    "tempmailaddress.com",
    "mailcatch.com",
    "emailondeck.com",
    "tempmailer.com",
    "opayq.com",
    "grr.la",
    "mailnull.com",
    "yopmail.com",
    "tempinbox.com",
    "bugmenot.com",
    "tmail.com",
    "discardmail.com",
    "e-mail.com",
    "gawab.com",
    "email.net",
    "mailbucket.org"
    "mailcat.biz",
    "disposableemail.org",
    "emailondeck.com",
    "emailondeck.org",
    "mailchop.com",
    "mailcker.com",
    "maildax.me",
    "mailde.de",
    "mailde.info",
    "maildrop.cf",
    "maildrop.ga",
    "maildrop.gq",
    "maildrop.ml",
    "maildu.de",
    "maildx.com",
    "maileater.com"
]
banned_domains_set = set(banned_domains_to_block)




actblue_to_datahub_underscore = {
    'firstname':"first_name",
    'lastname':"last_name",
    "addr1":"address",
    "full_name":"full_name",
    "city":"city",
    "state":"state",
    "stateCode":"state_code",
    "isEligibleForExpressLane":"is_eligible_for_express_lane",
    "email":"email",
    "phone":"phone_number",
    "countryCode":"country_code",
    "providedPhone":"provided_phone",
    "providedEmail":"provided_email",
    "employerData":"employer_data",
    "employerAddr1":"employer_address",
    "employerCity":"employer_city",
    "employerState":"employer_state",
    "employerStateCode":"employer_state_code",
    "employerCountry":"employer_country",
    "providedOccupation":"provided_occupation",
    "providedEmployer":"provided_employer",
    "zip4":"zip_4"
}



employer_llm_long_prime_conversation_array_start = [
    {"role":"system","content":"""I'm going to provide a company name that a user provided in a form submission. This employer name could be slightly different between user submissions. Since this is user input it can't be trusted and we must clean and filter.
I will give you a company name. You will respond with an updated and correct company name. Normalize and clean the inputs for global consistency. Use the most common spelling and capitalization pattern. Fix typos. Remove extra spacing and punctuation. For abbreviations like LLC and Inc. use correct abbreviation, punctuation, and capitalization.
If there is profanity or it's clearly not a real company return 'None'. If the user is trying to say they are not employed, reply 'Not Employed' . If the user is trying to say they are self employed or own their own company reply 'Self Employed'
Do not respond with your reasoning. Do not preface the response. Do not self-reference or mention anything about your knowledge or dates of your training data. Do not give excuses. If you do not know the answer or can't give a response simply response with only 'None'
Respond in plain text with no markings. Do not write more than the correctly formatted company name. Do not put your response in quotes. Use correct punctuation. Remember that some company names can be all capital letters or have no capital letters.
VERY IMPORTANT: Return ONLY the company name and nothing else."""},
{"role":"user","content":"Clean & normalize this company name: Apple"},
{"role":"system","content":"Apple Inc."},
{"role":"user","content":"Clean & normalize this company name: amazon.com"},
{"role":"system","content":"Amazon"},
{"role":"user","content":"Clean & normalize this company name: not-employed"},
{"role":"system","content":"Not Employed"},
{"role":"user","content":"Clean & normalize this company name: asdf"},
{"role":"system","content":"None"},
{"role":"user","content":"Clean & normalize this company name: fuck you"},
{"role":"system","content":"None"},
{"role":"user","content":"Clean & normalize this company name: n/a"},
{"role":"system","content":"Not Employed"},
{"role":"user","content":"Clean & normalize this company name: Brownstein Hyatt"},
{"role":"system","content":"Brownstein Hyatt Farber Schreck LLP"},
{"role":"user","content":"Clean & normalize this company name: Google, inc"},
{"role":"system","content":"Google"},
{"role":"user","content":"Clean & normalize this company name: UCLA"},
{"role":"system","content":"University of California Los Angeles"},
{"role":"user","content":"Clean & normalize this company name: univ. of arizona"},
{"role":"system","content":"University of Arizona"},
{"role":"user","content":"Clean & normalize this company name: Dept Veterans Affairs"},
{"role":"system","content":"U.S. Department of Veterans Affairs"}
]


person_format = {

    "voter_id":{
        "type":"str"
    },
    "ngpvan_id":{
        "type":"str"
    },
    "voter_registration_state_code":{
        "type":"str",
        "length":2,
        "case":"upper",
        "alpha_only":True
    },

    "first_name":{
        "case":"names_title_case",
        "type":"str",
        "exclude_chars":'[!@#$%^&*()_=+`~,./?<>?;:\'"[\]{}\\|0-9]',
        "remove_profanity":True,
        "strip_strings":True
    },
    "middle_name":{
         "case":"names_title_case",
        "type":"str",
        "exclude_chars":'[!@#$%^&*()_=+`~,./?<>?;:\'"[\]{}\\|0-9]',
        "remove_profanity":True,
        "strip_strings":True
    },
    "last_name":{
        "case":"names_title_case",
        "type":"str",
        "exclude_chars":'[!@#$%^&*()_=+`~,./?<>?;:\'"[\]{}\\|0-9]',
        "remove_profanity":True,
        "strip_strings":True
    },
    "full_name":{
        "case":"names_title_case",
        "type":"str",
        "exclude_chars":'[!@#$%^&*()_=+`~,./?<>?;:\'"[\]{}\\|0-9]',
        "remove_profanity":True,
        "strip_strings":True
    },
    "middle_initial":{
        "case":"upper",
        "type":"str",
        "length":1,
        "alpha_only":True
    },
    "last_initial":{
        "case":"upper",
        "type":"str",
        "length":1,
        "alpha_only":True
    },
    "first_initial":{
        "case":"upper",
        "type":"str",
        "length":1,
        "alpha_only":True
    },
    
    "suffix":{
        "type":"str"
    },
    
    "birth_year":{
        "type":"int",
        "length":4
    },

    "formatted_address": {
        "type":"str",
        #TODO think about this its kind of dumb
        # https://stackoverflow.com/questions/52179465/best-and-clean-way-to-encode-emojis-python-from-text-file
        "exclude_chars":"[=+~!@$%^*/()?;:<>[]"
    },
    "street_number": {
        "type":"str"
    },
    "route": {
        "type":"str"
    },
    "neighborhood": {
        "type":"str"
    },
    "locality":{
        "case":"title",
        "type":"str"
    },

    "administrative_area_level_2": {
        "type":"str"
    },
    "administrative_area_level_1": {
        "type":"str"
    },

    


    "recipient": {
        "type":"str"
    },
    "street_number": {
        "type":"str"
    },
    "street_number_prefix": {
        "type":"str"
    },
    "street_number_suffix": {
        "type":"str"
    },
    "route": {
        "type":"str"
    },
    "route_pre_directional": {
        "type":"str"
    },
    "route_pre_modifier": {
        "type":"str"
    },
    "route_pre_type": {
        "type":"str"
    },
    "route_post_directional": {
        "type":"str"
    },
    "route_post_modifier": {
        "type":"str"
    },
    "route_post_type": {
        "type":"str"
    },
    "corner_of": {
        "type":"str"
    },
    "intersection_separator": {
        "type":"str"
    },
    "landmark_name": {
        "type":"str"
    },
    "usps_box_group_id": {
        "type":"str"
    },
    "usps_box_group_type": {
        "type":"str"
    },
    "usps_box_id": {
        "type":"str"
    },
    "usps_box_type": {
        "type":"str"
    },
    "building_name": {
        "type":"str"
    },
    "occupancy_type": {
        "type":"str"
    },
    "occupancy_identifier": {
        "type":"str"
    },
    "subaddress_identifier": {
        "type":"str"
    },
    "subaddress_type": {
        "type":"str"
    },
    "city": {
        "type":"str"
    },
    "state": {
        "type":"str"
    },
    "zip": {
        "type":"str"
    },
    "not_address": {
        "type":"str"
    },
    "zip_4": {
        "type":"str"
    },
    "address": {
        "type":"str"
    },
    "address_2": {
        "type":"str"
    },







    "address":{
        "case":"title",
        "type":"str",
        "exclude_chars":"[=~!@$%^*\\/()_?;:<>[]"
    },
    "address_2":{
        "case":"title",
        "type":"str",
        "exclude_chars":"[=~!@$%^*\\/()_?;:<>[]"
    },
    "city":{
        "case":"title",
        "type":"str",
        "alpha_only":True,
        "exclude_chars":"[0-9=+~!@#$%^*\\/()_?;:<>[]"
    },
    "state":{
        "case":"title",
        "type":"str",
        "alpha_only":True,
        #TODO i think state is already fixed to correct ones only ?

    },
    "state_code":{
        "case":"upper",
        "type":"str",
        "length":2,
        "alpha_only":True
    },
    "county":{
        "case":"title",
        "type":"str",
        "alpha_only":True
    },
    "country":{
        "case":"title",
        "type":"str",
        "alpha_only":True
    },

    "country_code": {
        "type":"str",
        "length":2,
        "case":"upper",
        "alpha_only":True
    },

    "zip":{
        "type":"str",
        "length":5
    },
    "zip_4":{
        "type":"str",
        "length":4
    },
    "latitude":{
        "type":"float"
    },
    "longitude":{
        "type":"float"
    },

    #location_point TODO geo format from lat lon ?

    "google_place_id": {
        "type":"str"
    },

    "email":{
        "case":"lower",
        "type":"str"
    },
    "work_email":{
        "case":"lower",
        "type":"str"
    },
    "verified_email":{
        "type":"bool"
    },
        "email_mx_valid_check":{
        "type":"bool"
    },
    "email_smtp_valid_check":{
        "type":"bool"
    },
    "cell_phone":{
        "type":"str",
        "format":"phone"
    },
    "primary_cell_phone":{
        "type":"str",
        "format":"phone"
    },
    "primary_phone_number":{
        "type":"str",
        "format":"phone"
    },
    "phone_number":{
        "type":"str",
        "format":"phone"
    },
    "work_phone_number":{
        "type":"str",
        "format":"phone"
    },
    "landline":{
        "type":"str",
        "format":"phone"
    },
    "is_twilio_verified_cell":{
        "type":"bool"
    },
    "is_twilio_tcpa_on_dnc_list":{
        "type":"bool"
    },
    "dnc_list":{
        "type":"bool"
    },

    "title":{
        "case":"title",
        "type":"str",
        "min_length":2,
        "exclude_chars":"[0-9=+~!@#$%^*\\/()_?;:<>[]"
    },


    "birth_month": {
        "type":"int",
        "max_length":2
    },
    "birth_day": {
        "type":"int",
        "max_length":2
    },

    "provided_email":{
        "case":"lower",
        "type":"str"
    },

    #custom_data
    "email_unsubscribe":{
        "type":"bool"
    },
    "email_spamtrap":{
        "type":"bool"
    },

    "zerbounce_email_status": {
        "type":"str"
    },
    "zerobounce_email_substatus": {
        "type":"str"
    },


    "employer":{
        #"case":"title",was changing things we dont want like NIH -> Nih
        "type":"str",
        #"exclude_chars":None
    },
    "occupation":{
        "case":"title",
        "type":"str",
        #TODO look in bq for odd ones?
        #"alpha_only":True
        "exclude_chars":"[=+~!@#$%^*/()?;:<>[]"
    },
    "job_title":{
        "case":"title",
        "type":"str",
        "alpha_only":True
    },
    "employer_address":{
        "case":"title",
        "type":"str",
        "exclude_chars":"[=+~!@$%^*/()?;:<>[]"
    },
    "employer_address_2":{
        "case":"title",
        "type":"str",
        "exclude_chars":"[=~!@$%^*/()?;:<>[]"
    },
    "employer_city":{
        "case":"title",
        "type":"str",
        "exclude_chars":"[=+~!@#$%^*/()?;:<>[]"
    },
    "employer_state":{
        "case":"title",
        "type":"str",
        "alpha_only":True,
        #"exclude_chars":'-=+_~`!@$%^&*()_+;:\'\",./<>?'
    },
    "employer_country":{
        "case":"title",
        "type":"str",
        "alpha_only":True,
        #"exclude_chars":'-=+_~`!@$%^&*()_+;:\'\",./<>?'
    },
        "employer_zip":{
        "case":"title",
        "type":"str"
    },
        "employer_zip_4":{
        "case":"title",
        "type":"str"
    },

    #TODO zip_4 from employer split

    "employer_address_google_place_id": {
        "type":"str"
    },
    "gender":{
        "case":"upper",
        "type":"str",
        #TODO acceptable values
        "alpha_only":True,
        "exclude_chars":"[a-zA-Z]"
    },
    "gender_modeled":{
        "case":"upper",
        "type":"str",
        "options":["MALE","FEMALE","OTHER","NON-BINARY","GENDER-FLUID"]
    },

    #TODO ??
    #timezone float

    "spanish":{
        "type":"bool"
    },
    "sms_optin":{
        "type":"bool"
    },

    #fb_app_ids
    "ip" : {
        "type":"str"
    },
    "ipv6": {
        "type":"str"
    },
    "linkedin_url": {
        "type":"str"
    },
    "linkedin_username": {
        "type":"str"
    },
    "linkedin_id": {
        "type":"str"
    },
    "facebook_url": {
        "type":"str"
    },
    "facebook_username": {
        "type":"str"
    },
    "facebook_id": {
        "type":"str"
    },
    "twitter_url": {
        "type":"str"
    },
    "twitter_username": {
        "type":"str"
    },
    "github_url": {
        "type":"str"
    },
    "github_username": {
        "type":"str"
    },
    "people_data_labs_likely_id": {
        "type":"str"
    },
    "people_data_labs_likelihood": {
        "type":"str"
    },
    "school": {
        "type":"str"
    },
    "lifetime_donation_amount":{
        "type":"float"
    },
    "last_donation_amount":{
        "type":"float"
    },
        "last_donation_date":{
        "type":"timestamp"
    },
    
    "first_donation_date":{
        "type":"timestamp"
    },
    "average_donation_amount":{
        "type":"float"
    },
    "total_donations_count":{
        "type":"integer"
    },
    "is_eligible_for_express_lane":{
        "type":"bool"
    },

    "provided_employer":{
        "type":"str"
    },
    "provided_occupation":{
        "type":"str"
    },
    "employer_zip_4": {
        "type":"str",
        "max_length":4
    },
    "employer_state_code": {
        "type":"str",
        "length":2,
        "case":"upper",
        "alpha_only":True
    },
    "employer_country_code": {
        "type":"str",
        #???? see country code above
        #"max_length":5,
        "case":"upper"
    },

    "country_code": {
        "case":"upper",
        "type":"str",
        "length":2,
        "alpha_only":True
    },


}
