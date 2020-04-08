
import atmosrt



# def test_smarts():
# 	# very basic test
# 	moderate_model = atmosrt.SMARTS(atmosrt.settings.pollution['moderate'])
# 	print(moderate_model.spectrum())


def test_sbdart():
	# very basic test
	moderate_model = atmosrt.SBdart(atmosrt.settings.pollution['moderate'])

	print(moderate_model.spectrum())
