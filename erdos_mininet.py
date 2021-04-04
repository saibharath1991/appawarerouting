from mininet.topo import Topo
class MyTopo( Topo ):
	"Erdos topology experiment"

	def build (self): 
		"custom topology "

		mH_1 = self.addHost('h1')
		mS_1_11 = self.addSwitch('s11')
		self.addLink(mH_1, mS_1_11)
		mH_2 = self.addHost('h2')
		mS_2_22 = self.addSwitch('s22')
		self.addLink(mS_2_22, mH_2)
		self.addLink(mS_1_11, mS_2_22)
		mH_3 = self.addHost('h3')
		mS_3_32 = self.addSwitch('s32')
		self.addLink(mS_3_32, mH_3)
		self.addLink(mS_1_11, mS_3_32)
		mS_2_21 = self.addSwitch('s21')
		self.addLink(mH_2, mS_2_21)
		self.addLink(mS_2_21, mS_3_32)
		mH_4 = self.addHost('h4')
		mS_4_42 = self.addSwitch('s42')
		self.addLink(mS_4_42, mH_4)
		self.addLink(mS_2_21, mS_4_42)
		mS_3_31 = self.addSwitch('s31')
		self.addLink(mH_3, mS_3_31)
		self.addLink(mS_3_31, mS_4_42)
		mH_5 = self.addHost('h5')
		mS_5_52 = self.addSwitch('s52')
		self.addLink(mS_5_52, mH_5)
		self.addLink(mS_3_31, mS_5_52)
		mS_4_41 = self.addSwitch('s41')
		self.addLink(mH_4, mS_4_41)
		self.addLink(mS_4_41, mS_5_52)
		mH_6 = self.addHost('h6')
		mS_6_62 = self.addSwitch('s62')
		self.addLink(mS_6_62, mH_6)
		self.addLink(mS_4_41, mS_6_62)
		mS_5_51 = self.addSwitch('s51')
		self.addLink(mH_5, mS_5_51)
		self.addLink(mS_5_51, mS_6_62)
		mH_7 = self.addHost('h7')
		mS_7_72 = self.addSwitch('s72')
		self.addLink(mS_7_72, mH_7)
		self.addLink(mS_5_51, mS_7_72)
		mS_6_61 = self.addSwitch('s61')
		self.addLink(mH_6, mS_6_61)
		self.addLink(mS_6_61, mS_7_72)
		mH_8 = self.addHost('h8')
		mS_8_82 = self.addSwitch('s82')
		self.addLink(mS_8_82, mH_8)
		self.addLink(mS_6_61, mS_8_82)
		mS_7_71 = self.addSwitch('s71')
		self.addLink(mH_7, mS_7_71)
		self.addLink(mS_7_71, mS_8_82)
		mH_9 = self.addHost('h9')
		mS_9_92 = self.addSwitch('s92')
		self.addLink(mS_9_92, mH_9)
		self.addLink(mS_7_71, mS_9_92)
		mS_8_81 = self.addSwitch('s81')
		self.addLink(mH_8, mS_8_81)
		self.addLink(mS_8_81, mS_9_92)
		mH_10 = self.addHost('h10')
		mS_10_102 = self.addSwitch('s102')
		self.addLink(mS_10_102, mH_10)
		self.addLink(mS_8_81, mS_10_102)
		mS_9_91 = self.addSwitch('s91')
		self.addLink(mH_9, mS_9_91)
		self.addLink(mS_9_91, mS_10_102)
		mH_11 = self.addHost('h11')
		mS_11_112 = self.addSwitch('s112')
		self.addLink(mS_11_112, mH_11)
		self.addLink(mS_9_91, mS_11_112)
		mS_10_101 = self.addSwitch('s101')
		self.addLink(mH_10, mS_10_101)
		mH_12 = self.addHost('h12')
		mS_12_122 = self.addSwitch('s122')
		self.addLink(mS_12_122, mH_12)
		self.addLink(mS_10_101, mS_12_122)
		mS_11_111 = self.addSwitch('s111')
		self.addLink(mH_11, mS_11_111)
		self.addLink(mS_11_111, mS_12_122)
		mH_13 = self.addHost('h13')
		mS_13_132 = self.addSwitch('s132')
		self.addLink(mS_13_132, mH_13)
		self.addLink(mS_11_111, mS_13_132)
		mS_12_121 = self.addSwitch('s121')
		self.addLink(mH_12, mS_12_121)
		self.addLink(mS_12_121, mS_13_132)
		mH_14 = self.addHost('h14')
		mS_14_142 = self.addSwitch('s142')
		self.addLink(mS_14_142, mH_14)
		self.addLink(mS_12_121, mS_14_142)
		mS_13_131 = self.addSwitch('s131')
		self.addLink(mH_13, mS_13_131)
		self.addLink(mS_13_131, mS_14_142)
		mH_15 = self.addHost('h15')
		mS_15_152 = self.addSwitch('s152')
		self.addLink(mS_15_152, mH_15)
		self.addLink(mS_13_131, mS_15_152)
		mS_14_141 = self.addSwitch('s141')
		self.addLink(mH_14, mS_14_141)
		self.addLink(mS_14_141, mS_15_152)
		mH_16 = self.addHost('h16')
		mS_16_162 = self.addSwitch('s162')
		self.addLink(mS_16_162, mH_16)
		self.addLink(mS_14_141, mS_16_162)
		mS_15_151 = self.addSwitch('s151')
		self.addLink(mH_15, mS_15_151)
		self.addLink(mS_15_151, mS_16_162)
		mH_17 = self.addHost('h17')
		mS_17_172 = self.addSwitch('s172')
		self.addLink(mS_17_172, mH_17)
		self.addLink(mS_15_151, mS_17_172)
		mS_16_161 = self.addSwitch('s161')
		self.addLink(mH_16, mS_16_161)
		self.addLink(mS_16_161, mS_17_172)
		mH_18 = self.addHost('h18')
		mS_18_182 = self.addSwitch('s182')
		self.addLink(mS_18_182, mH_18)
		self.addLink(mS_16_161, mS_18_182)
		mS_17_171 = self.addSwitch('s171')
		self.addLink(mH_17, mS_17_171)
		self.addLink(mS_17_171, mS_18_182)
		mH_19 = self.addHost('h19')
		mS_19_192 = self.addSwitch('s192')
		self.addLink(mS_19_192, mH_19)
		self.addLink(mS_17_171, mS_19_192)
		mS_18_181 = self.addSwitch('s181')
		self.addLink(mH_18, mS_18_181)
		self.addLink(mS_18_181, mS_19_192)
		mH_20 = self.addHost('h20')
		mS_20_202 = self.addSwitch('s202')
		self.addLink(mS_20_202, mH_20)
		self.addLink(mS_18_181, mS_20_202)
		mS_19_191 = self.addSwitch('s191')
		self.addLink(mH_19, mS_19_191)
		self.addLink(mS_19_191, mS_20_202)
		mH_21 = self.addHost('h21')
		mS_21_212 = self.addSwitch('s212')
		self.addLink(mS_21_212, mH_21)
		self.addLink(mS_19_191, mS_21_212)
		mS_20_201 = self.addSwitch('s201')
		self.addLink(mH_20, mS_20_201)
		self.addLink(mS_20_201, mS_21_212)
		mH_22 = self.addHost('h22')
		mS_22_222 = self.addSwitch('s222')
		self.addLink(mS_22_222, mH_22)
		self.addLink(mS_20_201, mS_22_222)
		mS_21_211 = self.addSwitch('s211')
		self.addLink(mH_21, mS_21_211)
		self.addLink(mS_21_211, mS_22_222)
		mH_23 = self.addHost('h23')
		mS_23_232 = self.addSwitch('s232')
		self.addLink(mS_23_232, mH_23)
		self.addLink(mS_21_211, mS_23_232)
		mS_22_221 = self.addSwitch('s221')
		self.addLink(mH_22, mS_22_221)
		mH_24 = self.addHost('h24')
		mS_24_242 = self.addSwitch('s242')
		self.addLink(mS_24_242, mH_24)
		self.addLink(mS_22_221, mS_24_242)
		mH_47 = self.addHost('h47')
		mS_47_472 = self.addSwitch('s472')
		self.addLink(mS_47_472, mH_47)
		self.addLink(mS_22_221, mS_47_472)
		mS_23_231 = self.addSwitch('s231')
		self.addLink(mH_23, mS_23_231)
		self.addLink(mS_23_231, mS_24_242)
		mH_25 = self.addHost('h25')
		mS_25_252 = self.addSwitch('s252')
		self.addLink(mS_25_252, mH_25)
		self.addLink(mS_23_231, mS_25_252)
		mS_24_241 = self.addSwitch('s241')
		self.addLink(mH_24, mS_24_241)
		self.addLink(mS_24_241, mS_25_252)
		mH_26 = self.addHost('h26')
		mS_26_262 = self.addSwitch('s262')
		self.addLink(mS_26_262, mH_26)
		self.addLink(mS_24_241, mS_26_262)
		mS_25_251 = self.addSwitch('s251')
		self.addLink(mH_25, mS_25_251)
		self.addLink(mS_25_251, mS_26_262)
		mH_27 = self.addHost('h27')
		mS_27_272 = self.addSwitch('s272')
		self.addLink(mS_27_272, mH_27)
		self.addLink(mS_25_251, mS_27_272)
		mS_26_261 = self.addSwitch('s261')
		self.addLink(mH_26, mS_26_261)
		self.addLink(mS_26_261, mS_27_272)
		mH_28 = self.addHost('h28')
		mS_28_282 = self.addSwitch('s282')
		self.addLink(mS_28_282, mH_28)
		self.addLink(mS_26_261, mS_28_282)
		mS_27_271 = self.addSwitch('s271')
		self.addLink(mH_27, mS_27_271)
		self.addLink(mS_27_271, mS_28_282)
		mH_29 = self.addHost('h29')
		mS_29_292 = self.addSwitch('s292')
		self.addLink(mS_29_292, mH_29)
		self.addLink(mS_27_271, mS_29_292)
		mS_28_281 = self.addSwitch('s281')
		self.addLink(mH_28, mS_28_281)
		self.addLink(mS_28_281, mS_29_292)
		mH_30 = self.addHost('h30')
		mS_30_302 = self.addSwitch('s302')
		self.addLink(mS_30_302, mH_30)
		self.addLink(mS_28_281, mS_30_302)
		mS_29_291 = self.addSwitch('s291')
		self.addLink(mH_29, mS_29_291)
		self.addLink(mS_29_291, mS_30_302)
		mH_31 = self.addHost('h31')
		mS_31_312 = self.addSwitch('s312')
		self.addLink(mS_31_312, mH_31)
		self.addLink(mS_29_291, mS_31_312)
		mS_30_301 = self.addSwitch('s301')
		self.addLink(mH_30, mS_30_301)
		self.addLink(mS_30_301, mS_31_312)
		mH_32 = self.addHost('h32')
		mS_32_322 = self.addSwitch('s322')
		self.addLink(mS_32_322, mH_32)
		self.addLink(mS_30_301, mS_32_322)
		mS_31_311 = self.addSwitch('s311')
		self.addLink(mH_31, mS_31_311)
		self.addLink(mS_31_311, mS_32_322)
		mH_33 = self.addHost('h33')
		mS_33_332 = self.addSwitch('s332')
		self.addLink(mS_33_332, mH_33)
		self.addLink(mS_31_311, mS_33_332)
		mS_32_321 = self.addSwitch('s321')
		self.addLink(mH_32, mS_32_321)
		self.addLink(mS_32_321, mS_33_332)
		mH_34 = self.addHost('h34')
		mS_34_342 = self.addSwitch('s342')
		self.addLink(mS_34_342, mH_34)
		self.addLink(mS_32_321, mS_34_342)
		mS_33_331 = self.addSwitch('s331')
		self.addLink(mH_33, mS_33_331)
		self.addLink(mS_33_331, mS_34_342)
		mH_35 = self.addHost('h35')
		mS_35_352 = self.addSwitch('s352')
		self.addLink(mS_35_352, mH_35)
		self.addLink(mS_33_331, mS_35_352)
		mS_34_341 = self.addSwitch('s341')
		self.addLink(mH_34, mS_34_341)
		self.addLink(mS_34_341, mS_35_352)
		mH_36 = self.addHost('h36')
		mS_36_362 = self.addSwitch('s362')
		self.addLink(mS_36_362, mH_36)
		self.addLink(mS_34_341, mS_36_362)
		mS_35_351 = self.addSwitch('s351')
		self.addLink(mH_35, mS_35_351)
		self.addLink(mS_35_351, mS_36_362)
		mH_37 = self.addHost('h37')
		mS_37_372 = self.addSwitch('s372')
		self.addLink(mS_37_372, mH_37)
		self.addLink(mS_35_351, mS_37_372)
		mS_36_361 = self.addSwitch('s361')
		self.addLink(mH_36, mS_36_361)
		self.addLink(mS_36_361, mS_37_372)
		mS_37_371 = self.addSwitch('s371')
		self.addLink(mH_37, mS_37_371)
		mH_38 = self.addHost('h38')
		mS_38_382 = self.addSwitch('s382')
		self.addLink(mS_38_382, mH_38)
		self.addLink(mS_37_371, mS_38_382)
		mH_39 = self.addHost('h39')
		mS_39_392 = self.addSwitch('s392')
		self.addLink(mS_39_392, mH_39)
		self.addLink(mS_37_371, mS_39_392)
		mS_38_381 = self.addSwitch('s381')
		self.addLink(mH_38, mS_38_381)
		self.addLink(mS_38_381, mS_39_392)
		mH_40 = self.addHost('h40')
		mS_40_402 = self.addSwitch('s402')
		self.addLink(mS_40_402, mH_40)
		self.addLink(mS_38_381, mS_40_402)
		mS_39_391 = self.addSwitch('s391')
		self.addLink(mH_39, mS_39_391)
		self.addLink(mS_39_391, mS_40_402)
		mH_41 = self.addHost('h41')
		mS_41_412 = self.addSwitch('s412')
		self.addLink(mS_41_412, mH_41)
		self.addLink(mS_39_391, mS_41_412)
		mS_40_401 = self.addSwitch('s401')
		self.addLink(mH_40, mS_40_401)
		self.addLink(mS_40_401, mS_41_412)
		mH_42 = self.addHost('h42')
		mS_42_422 = self.addSwitch('s422')
		self.addLink(mS_42_422, mH_42)
		self.addLink(mS_40_401, mS_42_422)
		mS_41_411 = self.addSwitch('s411')
		self.addLink(mH_41, mS_41_411)
		self.addLink(mS_41_411, mS_42_422)
		mH_43 = self.addHost('h43')
		mS_43_432 = self.addSwitch('s432')
		self.addLink(mS_43_432, mH_43)
		self.addLink(mS_41_411, mS_43_432)
		mS_42_421 = self.addSwitch('s421')
		self.addLink(mH_42, mS_42_421)
		self.addLink(mS_42_421, mS_43_432)
		mH_44 = self.addHost('h44')
		mS_44_442 = self.addSwitch('s442')
		self.addLink(mS_44_442, mH_44)
		self.addLink(mS_42_421, mS_44_442)
		mS_43_431 = self.addSwitch('s431')
		self.addLink(mH_43, mS_43_431)
		self.addLink(mS_43_431, mS_44_442)
		mH_45 = self.addHost('h45')
		mS_45_452 = self.addSwitch('s452')
		self.addLink(mS_45_452, mH_45)
		self.addLink(mS_43_431, mS_45_452)
		mS_44_441 = self.addSwitch('s441')
		self.addLink(mH_44, mS_44_441)
		self.addLink(mS_44_441, mS_45_452)
		mH_46 = self.addHost('h46')
		mS_46_462 = self.addSwitch('s462')
		self.addLink(mS_46_462, mH_46)
		self.addLink(mS_44_441, mS_46_462)
		mS_45_451 = self.addSwitch('s451')
		self.addLink(mH_45, mS_45_451)
		self.addLink(mS_45_451, mS_46_462)
		self.addLink(mS_45_451, mS_47_472)
		mS_46_461 = self.addSwitch('s461')
		self.addLink(mH_46, mS_46_461)
		self.addLink(mS_46_461, mS_47_472)
		mH_48 = self.addHost('h48')
		mS_48_482 = self.addSwitch('s482')
		self.addLink(mS_48_482, mH_48)
		self.addLink(mS_46_461, mS_48_482)
		mS_47_471 = self.addSwitch('s471')
		self.addLink(mH_47, mS_47_471)
		self.addLink(mS_47_471, mS_48_482)
		mS_48_481 = self.addSwitch('s481')
		self.addLink(mH_48, mS_48_481)
		mH_50 = self.addHost('h50')
		mS_50_502 = self.addSwitch('s502')
		self.addLink(mS_50_502, mH_50)
		self.addLink(mS_48_481, mS_50_502)
		mH_49 = self.addHost('h49')
		mS_49_491 = self.addSwitch('s491')
		self.addLink(mH_49, mS_49_491)
		self.addLink(mS_49_491, mS_50_502)

topos = { 'mytopo': ( lambda: MyTopo() ) }