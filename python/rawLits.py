#!/usr/bin/python
# -*-coding:utf-8 -*-

rawLits=[{"lit":"#", "cat":"A", "ln":1,  "soundPrototypes":{"C":"h","V":"e"}},
{"lit":"hu", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"cs", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"k","V":None}},
{"lit":"aƿ", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aw"}},
{"lit":"oƿ", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ow"}},
{"lit":"x", "cat":"C", "ln":1,  "soundPrototypes":{"C":"k","V":None}},
{"lit":"J", "cat":"A", "ln":1,  "soundPrototypes":{"C":"j","V":"i"}},
{"lit":"eæ", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"ey", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ᵹƿ", "cat":"C", "ln":2, "defaultDigraph":True},
{"lit":"hþ", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"hð", "cat":"C", "ln":2, "defaultDigraph":True},
{"lit":"ae", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"aj"}},
{"lit":"_", "cat":"A", "ln":1,  "soundPrototypes":{"C":None,"V":None}},
{"lit":"[]", "cat":"A", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":None}},
{"lit":"á", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"a:"}},
{"lit":"é", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"e:"}},
{"lit":"í", "cat":"A", "ln":1, "soundPrototypes":{"C":None,"V":"i:"}},
{"lit":"ó", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"o:"}},
{"lit":"ú", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"u:"}},
{"lit":"ý", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"y:"}},
{"lit":"ǣ", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"e:"}},
{"lit":"ðð", "cat":"C", "ln":2, "defaultDigraph":True},
{"lit":"vv", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"w","V":None}},
{"lit":"eea", "cat":"V", "ln":3, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"-", "cat":"-", "ln":1, "soundPrototypes":{"C":None,"V":None}},
         #FIX
{"lit":"ᵹh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ɣ","V":None}},
{"lit":"ȝw", "cat":"C", "ln":2, "defaultDigraph":False},
{"lit":"ȝȝ", "cat":"V", "ln":2, "defaultDigraph":True},
{"lit":"ᵹ", "cat":"C", "ln":1, "soundPrototypes":{"C":"ɣ","V":None}},
{"lit":"hw", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"hƿ", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"ƿh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"éo", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"oo", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ie", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"íe", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ia", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ye", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ya", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"t", "cat":"C", "ln":1, "soundPrototypes":{"C":"t","V":None}},
{"lit":"yh", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"h","V":None}},
{"lit":"ƿ", "cat":"C", "ln":1, "soundPrototypes":{"C":"p","V":None}},
{"lit":"rr", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"r","V":None}},
{"lit":"r", "cat":"C", "ln":1, "soundPrototypes":{"C":"r","V":None}},
{"lit":"ll", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"l","V":None}},
{"lit":"lll", "cat":"C", "ln":3, "defaultDigraph":True, "soundPrototypes":{"C":"l","V":None}},
{"lit":"l", "cat":"C", "ln":1, "soundPrototypes":{"C":"1","V":None}},
{"lit":"nn", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"n","V":None}},
{"lit":"n", "cat":"C", "ln":1, "soundPrototypes":{"C":"n","V":None}},
{"lit":"mm", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"m","V":None}},
{"lit":"m", "cat":"C", "ln":1, "soundPrototypes":{"C":"m","V":None}},
{"lit":"qw", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"qu", "cat":"C", "ln":2, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"quh", "cat":"C", "ln":3, "soundPrototypes":{"C":"ʍ","V":None}},
{"lit":"wh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"w","V":None}},
{"lit":"wƿ", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"w","V":None}},
{"lit":"gh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ɣ","V":None}},
{"lit":"ȝh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ɣ","V":None}},
{"lit":"h", "cat":"C", "ln":1, "soundPrototypes":{"C":"h","V":None}},
{"lit":"ssch", "cat":"C", "ln":4, "defaultDigraph":True, "soundPrototypes":{"C":"ʃ","V":None}},
{"lit":"ssh", "cat":"C", "ln":3, "defaultDigraph":True, "soundPrototypes":{"C":"ʃ","V":None}},
{"lit":"sc", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"ʃ","V":None}},
{"lit":"sch", "cat":"C", "ln":3, "defaultDigraph":True, "soundPrototypes":{"C":"ʃ","V":None}},
{"lit":"sh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"ʃ","V":None}},
{"lit":"z", "cat":"C", "ln":1, "soundPrototypes":{"C":"z","V":None}},
{"lit":"ȝ", "cat":"C", "ln":1, "soundPrototypes":{"C":"ɣ","V":None}},
{"lit":"s", "cat":"C", "ln":1, "soundPrototypes":{"C":"s","V":None}},
{"lit":"ss", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"s","V":None}},
{"lit":"thþ", "cat":"C", "ln":3, "defaultDigraph":True},
{"lit":"þþ", "cat":"C", "ln":2, "defaultDigraph":True},
{"lit":"th", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"θ","V":None}},
{"lit":"ð", "cat":"C", "ln":1, "soundPrototypes":{"C":"ð","V":None}},
{"lit":"þ", "cat":"C", "ln":1, "soundPrototypes":{"C":"θ","V":None}},
{"lit":"ph", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"f","V":None}},
{"lit":"ff", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"f","V":None}},
{"lit":"f", "cat":"C", "ln":1, "soundPrototypes":{"C":"f","V":None}},
{"lit":"gu", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"g","V":None}},
{"lit":"ʒ", "cat":"C", "ln":1, "soundPrototypes":{"C":"ɣ","V":None}},
{"lit":"dg", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"d","V":None}},
{"lit":"j", "cat":"A", "ln":1, "soundPrototypes":{"C":"j","V":"i"}},
{"lit":"ng", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"n","V":None}},
{"lit":"g", "cat":"C", "ln":1,  "soundPrototypes":{"C":"g","V":None}},
{"lit":"gg", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"g","V":None}},
{"lit":"dd", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"d","V":None}},
{"lit":"bb", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"b","V":None}},
{"lit":"b", "cat":"C", "ln":1, "soundPrototypes":{"C":"b","V":None}},
{"lit":"cu", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"k","V":None}},
{"lit":"ck", "cat":"C", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":"k","V":None}},
{"lit":"kk", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"k","V":None}},
{"lit":"q", "cat":"C", "ln":1, "soundPrototypes":{"C":"k","V":None}},
{"lit":"k", "cat":"C", "ln":1, "soundPrototypes":{"C":"k","V":None}},
{"lit":"cch", "cat":"C", "ln":3, "defaultDigraph":True, "soundPrototypes":{"C":"θ","V":None}},
{"lit":"ch", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"x":"θ","V":None}},
 {"lit":"hh", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"h","V":None}},
{"lit":"c", "cat":"C", "ln":1, "soundPrototypes":{"C":"k","V":None}},
{"lit":"tt", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"t","V":None}},
{"lit":"pp", "cat":"C", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":"p","V":None}},
{"lit":"p", "cat":"C", "ln":1, "soundPrototypes":{"C":"p","V":None}},
{"lit":"oy", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"oj"}},
{"lit":"oi", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"oj"}},
{"lit":"eaw", "cat":"V", "ln":3, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aw"}},
{"lit":"eouw", "cat":"V", "ln":4, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"yw", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"iu"}},
{"lit":"iu", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"iu"}},
{"lit":"w", "cat":"C", "ln":1, "soundPrototypes":{"C":"w","V":None}},
{"lit":"ew", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"eƿ", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"eow", "cat":"V", "ln":3, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"iw", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"iw"}},
{"lit":"aw", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aw"}},
{"lit":"au", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aw"}},
{"lit":"æȜ", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"aȜ", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aw"}},
{"lit":"eȜ", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ew"}},
{"lit":"æi", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ej"}},
#{"lit":"y-e", "cat":"V", "ln":3},
{"lit":"uy", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"uj"}},
{"lit":"ui", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"uj"}},
#{"lit":"u-e", "cat":"V", "ln":3},
{"lit":"ov", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ow"}},
{"lit":"ow", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ow"}},
{"lit":"uw", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"uw"}},
#{"lit":"o-e", "cat":"V", "ln":3},
{"lit":"ou", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ow"}},
{"lit":"oo", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"o:"}},
{"lit":"oa", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"oa"}},
{"lit":"ay", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aj"}},
{"lit":"ai", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"aj"}},
{"lit":"aa", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"a:"}},
#{"lit":"e-e", "cat":"V", "ln":3},
{"lit":"ee", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"e:"}},
{"lit":"éé", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"e"}},
{"lit":"eu", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ow"}},
{"lit":"eo", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ew"}},
#{"lit":"i-e", "cat":"V", "ln":3},
{"lit":"ei", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ey", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ej"}},
{"lit":"ij", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ij"}},
{"lit":"ii", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"i:"}},
{"lit":"v", "cat":"A", "ln":1, "soundPrototypes":{"C":"v","V":None}},
{"lit":"ea", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"e"}},
{"lit":"æ", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"e"}},
{"lit":"a", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"a"}},
{"lit":"e", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"v"}},
{"lit":"o", "cat":"V", "ln":1, "soundPrototypes":{"C":None,"V":"o"}},
{"lit":"oe", "cat":"V", "ln":2, "defaultDigraph":True, "soundPrototypes":{"C":None,"V":"ɵ"}},
{"lit":"ue", "cat":"V", "ln":2, "defaultDigraph":False, "soundPrototypes":{"C":None,"V":"ɵ"}},
{"lit":"u", "cat":"A", "ln":1, "soundPrototypes":{"C":"v","V":"u"}},
{"lit":"y", "cat":"A", "ln":1, "soundPrototypes":{"C":"j","V":"i"}},
{"lit":"i", "cat":"A", "ln":1, "soundPrototypes":{"C":"j","V":"i"}},
{"lit":"d", "cat":"C", "ln":1, "soundPrototypes":{"C":"d","V":None}},
        {"lit":"D", "cat":"C", "ln":1},
       {"lit":"dþ", "cat":"C", "ln":2, "defaultDigraph":True},
       {"lit":"tþ", "cat":"C", "ln":2, "defaultDigraph":True}
        ]

