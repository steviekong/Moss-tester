import mosspy
import sys

def get_moss_results(userid, basefile_name, testfiles_path ,language, report_path):
	moss_obj = mosspy.Moss(userid, language)

	moss_obj.addBaseFile(basefile_name)

	language_extensions = {
		"javascript" : "js",
		"python" : "py",
		"c++" : "cpp",
		"c" : "c",
		"java" : "java"
	}

	moss_obj.addFilesByWildcard(testfiles_path+"/*."+language_extensions[language])

	url = moss_obj.send()
	print ("Report Url: " + url)

	mosspy.download_report(url, report_path+"/report", connections = 8)


def main():
	if len(sys.argv) <  5:
		if sys.argv[1] is '--help':
			print("To run a moss test use:\n\'python moss.py <userid> <language> <basefile name> <testfiles directory path> <report directory>\'\nTestfiles must all be in the same directory!\nReport is generated in the same directory as the script!")
		else:
			print('Too few arguments!\nFormat is \'python moss.py <userid> <language> <basefile name> <testfiles directory path> <report directory>\'\nType \'python moss.py --help\' to get help.>\'')
		sys.exit(1)
	else:
		print(len(sys.argv))
		get_moss_results(userid = sys.argv[1], language = sys.argv[2], basefile_name = sys.argv[3], testfiles_path = sys.argv[4], report_path = sys.argv[5])

if __name__ == '__main__':
	main()

