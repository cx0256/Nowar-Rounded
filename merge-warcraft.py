import sys
import json
from fontlib.merge import MergeBelow
from fontlib.transform import Transform, ChangeAdvanceWidth

def NameFont(font, region, weight, version):

	isStdStyle = weight == 'Regular' or weight == 'Bold'

	font['OS_2']['achVendID'] = 'Cyan'
	font['name'] = [
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 0,
			"nameString": "Copyright © 2018—2019 Cyano Hao, with reserved font name “Nowar”, “有爱”, and “有愛”. Portions Copyright 2015 Google Inc. Portions © 2014, 2015, 2018 Adobe (http://www.adobe.com/)."
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 1,
			"nameString": "Nowar Warcraft Rounded {}".format(region) if isStdStyle else "Nowar Warcraft Rounded {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 2052,
			"nameID": 1,
			"nameString": "有爱魔兽圆体 {}".format(region) if isStdStyle else "有爱魔兽圆体 {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1028,
			"nameID": 1,
			"nameString": "有愛魔獸圓體 {}".format(region) if isStdStyle else "有愛魔獸圓體 {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 3076,
			"nameID": 1,
			"nameString": "有愛魔獸圓體 {}".format(region) if isStdStyle else "有愛魔獸圓體 {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 2,
			"nameString": weight if isStdStyle else "Regular"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 3,
			"nameString": "Nowar Warcraft Rounded {} {}".format(region, weight) + ' ' + str(version)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 4,
			"nameString": "Nowar Warcraft Rounded {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 2052,
			"nameID": 4,
			"nameString": "有爱魔兽圆体 {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1028,
			"nameID": 4,
			"nameString": "有愛魔獸圓體 {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 3076,
			"nameID": 4,
			"nameString": "有愛魔獸圓體 {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 5,
			"nameString": str(version)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 6,
			"nameString": "Nowar-Warcraft-Rounded-{}-{}".format(region, weight.replace(' ', '-'))
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 8,
			"nameString": "Cyano Hao"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 9,
			"nameString": "Cyano Hao (round all glyphs); Monotype Design Team (Latin, Greek & Cyrillic); Ryoko NISHIZUKA 西塚涼子 (kana, bopomofo & ideographs); Sandoll Communications 산돌커뮤니케이션, Soo-young JANG 장수영 & Joo-yeon KANG 강주연 (hangul elements, letters & syllables); Dr. Ken Lunde (project architect, glyph set definition & overall production); Masataka HATTORI 服部正貴 (production & ideograph elements)"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 11,
			"nameString": "https://github.com/CyanoHao"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 13,
			"nameString": "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software."
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 14,
			"nameString": "http://scripts.sil.org/OFL"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 16,
			"nameString": "Nowar Warcraft Rounded {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 2052,
			"nameID": 16,
			"nameString": "有爱魔兽圆体 {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1028,
			"nameID": 16,
			"nameString": "有愛魔獸圓體 {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 3076,
			"nameID": 16,
			"nameString": "有愛魔獸圓體 {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 17,
			"nameString": weight
		},
	]

if __name__ == '__main__':
	region = sys.argv[1]
	weight = sys.argv[2]
	encoding = sys.argv[3]
	version = sys.argv[4]

	with open("noto/rounded/NotoRounded-SemiCondensed{}.otd".format(weight), 'rb') as baseFile:
		baseFont = json.loads(baseFile.read().decode('UTF-8', errors='replace'))

	with open("noto/rounded/NotoRounded-Condensed{}.otd".format(weight), 'rb') as numFile:
		numFont = json.loads(numFile.read().decode('UTF-8', errors='replace'))

	with open("rhr/ResourceHanRounded{}-{}.otd".format(region, weight), 'rb') as asianFile:
		asianFont = json.loads(asianFile.read().decode('UTF-8', errors = 'replace'))

	with open("noto/emoji/NotoEmoji-Regular.otd", 'rb') as emojiFile:
		emojiFont = json.loads(emojiFile.read().decode('UTF-8', errors = 'replace'))

	baseFont['OS_2']['ulCodePageRange1'][encoding] = True
	NameFont(baseFont, 'Classic' if region == 'CL' else region, weight, version)

	maxWidth = 490
	numWidth = numFont['glyf']['zero']['advanceWidth']
	changeWidth = maxWidth - numWidth if numWidth > maxWidth else 0

	for n in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
		glyph = numFont['glyf'][n]
		width = glyph['advanceWidth']
		pGlyph = numFont['glyf'][n + '.lf']
		pWidth = pGlyph['advanceWidth']
		if pWidth < width:
			glyph = pGlyph
			width = pWidth
		if changeWidth != 0:
			ChangeAdvanceWidth(glyph, changeWidth)
			Transform(glyph, 1, 0, 0, 1, (changeWidth + 1) // 2, 0)
		baseFont['glyf'][n] = glyph

	MergeBelow(baseFont, asianFont)
	for _, glyph in emojiFont['glyf'].items():
		Transform(glyph, 1000 / 2048, 0, 0, 1000 / 2048, 0, 0)
	MergeBelow(baseFont, emojiFont)

	# quotes, em-dash and ellipsis
	for u in [0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026]:
		if str(u) in asianFont['cmap']:
			baseFont['glyf'][baseFont['cmap'][str(u)]] = asianFont['glyf'][asianFont['cmap'][str(u)]]

	outStr = json.dumps(baseFont, ensure_ascii=False)
	with open("nowar/{}-NowarWarcraftRounded-{}-{}.otd".format(encoding, region, weight), 'w') as outFile:
		outFile.write(outStr)
