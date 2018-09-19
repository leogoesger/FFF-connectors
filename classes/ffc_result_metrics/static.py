metric_names = [
    "Year",
    "Avg",
    "Std",
    "CV",
    "SP_Tim",
    "SP_Mag",
    "SP_Dur",
    "SP_ROC",
    "DS_Tim",
    "DS_Mag_10",
    "DS_Mag_50",
    "DS_Dur_WSI",
    "DS_Dur_WS",
    "DS_No_Flow",
    "WSI_Tim",
    "WSI_Mag",
    "Wet_Tim",
    "WSI_Dur",
    "Wet_BFL_Mag",
    "Peak_Tim_2",
    "Peak_Dur_2",
    "Peak_Fre_2",
    "Peak_Mag_2",
    "Peak_Tim_5",
    "Peak_Dur_5",
    "Peak_Fre_5",
    "Peak_Mag_5",
    "Peak_Tim_10",
    "Peak_Dur_10",
    "Peak_Fre_10",
    "Peak_Mag_10",
    "Peak_Tim_20",
    "Peak_Dur_20",
    "Peak_Fre_20",
    "Peak_Mag_20",
]

gauge_reference = {
    "10295500": 1,
    "10308783": 1,
    "10281800": 1,
    "10291500": 1,
    "10308200": 1,
    "10310000": 1,
    "10336580": 1,
    "10336600": 1,
    "10336770": 1,
    "10336780": 1,
    "11208000": 1,
    "11213500": 1,
    "11214000": 1,
    "11218500": 1,
    "11226500": 1,
    "11230500": 1,
    "11237500": 1,
    "11264500": 1,
    "11266500": 1,
    "11274790": 1,
    "11275000": 1,
    "11292500": 1,
    "11294000": 1,
    "11418000": 2,
    "11251000": 2,
    "11270900": 2,
    "11299000": 2,
    "11446220": 2,
    "11419000": 2,
    "11406999": 2,
    "10264600": 3,
    "11196400": 3,
    "11204100": 3,
    "10255810": 3,
    "10257500": 3,
    "10257600": 3,
    "10258000": 3,
    "10258500": 3,
    "10259000": 3,
    "10259200": 3,
    "10263500": 3,
    "10264000": 3,
    "10336645": 3,
    "10336660": 3,
    "10336676": 3,
    "10340500": 3,
    "10343500": 3,
    "11031500": 3,
    "11033000": 3,
    "11037700": 3,
    "11063000": 3,
    "11073470": 3,
    "11080500": 3,
    "11082000": 3,
    "11094000": 3,
    "11095500": 3,
    "11111500": 3,
    "11113000": 3,
    "11154700": 3,
    "11195500": 3,
    "11203580": 3,
    "11208500": 3,
    "11209900": 3,
    "11220000": 3,
    "11268000": 3,
    "11281000": 3,
    "11282000": 3,
    "11283500": 3,
    "11294500": 3,
    "11315000": 3,
    "11316800": 3,
    "11318500": 3,
    "11341400": 3,
    "11376500": 3,
    "11394500": 3,
    "11400000": 3,
    "11408850": 3,
    "11409300": 3,
    "11409500": 3,
    "11413100": 3,
    "11413320": 3,
    "11414000": 3,
    "11426150": 3,
    "11427700": 3,
    "11433260": 3,
    "11433300": 3,
    "11433500": 3,
    "11445500": 3,
    "11472900": 3,
    "11480390": 3,
    "11522500": 3,
    "11523200": 3,
    "11525500": 3,
    "11526500": 3,
    "11527400": 3,
    "11154100": 4,
    "11390672": 4,
    "11396400": 4,
    "11413323": 4,
    "11457000": 4,
    "11458300": 4,
    "11467200": 4,
    "11467500": 4,
    "11467600": 4,
    "11468000": 4,
    "11468500": 4,
    "11468600": 4,
    "11468900": 4,
    "11472160": 4,
    "11473900": 4,
    "11474500": 4,
    "11475500": 4,
    "11475560": 4,
    "11475800": 4,
    "11476500": 4,
    "11476600": 4,
    "11477000": 4,
    "11477500": 4,
    "11478500": 4,
    "11481200": 4,
    "11481500": 4,
    "11482110": 4,
    "11482120": 4,
    "11482125": 4,
    "11482200": 4,
    "11482500": 4,
    "11529000": 4,
    "11532000": 4,
    "11532500": 4,
    "11377100": 5,
    "11269300": 6,
    "11110500": 6,
    "11115500": 6,
    "11117600": 6,
    "11117800": 6,
    "11120500": 6,
    "11124500": 6,
    "11128400": 6,
    "11141150": 6,
    "11141280": 6,
    "11143000": 6,
    "11143500": 6,
    "11148900": 6,
    "11151300": 6,
    "11151870": 6,
    "11152900": 6,
    "11153470": 6,
    "11153900": 6,
    "11156500": 6,
    "11159690": 6,
    "11160000": 6,
    "11160020": 6,
    "11160070": 6,
    "11160300": 6,
    "11160500": 6,
    "11162500": 6,
    "11162540": 6,
    "11162570": 6,
    "11169800": 6,
    "11180500": 6,
    "11180825": 6,
    "11180960": 6,
    "11181000": 6,
    "11181390": 6,
    "11182100": 6,
    "11182500": 6,
    "11183000": 6,
    "11197250": 6,
    "11199500": 6,
    "11220500": 6,
    "11274500": 6,
    "11274630": 6,
    "11337500": 6,
    "11371000": 6,
    "11372000": 6,
    "11375700": 6,
    "11449500": 6,
    "11451100": 6,
    "11460100": 6,
    "11464500": 6,
    "11473100": 6,
    "11480800": 6,
    "11522300": 6,
    "11525530": 6,
    "11525670": 6,
    "11528700": 6,
    "11116000": 7,
    "11120510": 7,
    "11120520": 7,
    "11120550": 7,
    "11132500": 7,
    "11138500": 7,
    "11172100": 7,
    "11172945": 7,
    "11173200": 7,
    "11176400": 7,
    "11224500": 7,
    "11253310": 7,
    "11379000": 8,
    "10255800": 8,
    "11023250": 8,
    "11023310": 8,
    "11023325": 8,
    "11046300": 8,
    "11046500": 8,
    "11048553": 8,
    "11058600": 8,
    "11077000": 8,
    "11084500": 8,
    "11098000": 8,
    "11100000": 8,
    "11120530": 8,
    "11134800": 8,
    "11257500": 8,
    "11258000": 8,
    "11259000": 8,
    "11284400": 8,
    "11299600": 8,
    "11334300": 8,
    "11374000": 8,
    "11451715": 8,
    "10360900": 9,
    "11355500": 9,
}
