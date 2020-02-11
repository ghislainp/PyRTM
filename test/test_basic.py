
import rtm



def test_smarts():
	# very basic test
	moderate_model = rtm.SMARTS(rtm.settings.pollution['moderate'])
	print(moderate_model.spectrum())


def test_sbdart():
	# very basic test
	moderate_model = rtm.SBdart(rtm.settings.pollution['moderate'])

	print(moderate_model.spectrum())
