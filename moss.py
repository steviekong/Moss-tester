import mosspy
import sys

def get_moss_results(userid, basefile_name, testfiles_path ,language, report_path):
	real_language = None
	if language == 'html': 
		real_language = 'javascript'
	else: 
		real_language = language
	moss_obj = mosspy.Moss(userid, real_language)

	moss_obj.addBaseFile(basefile_name)

	language_extensions = {
		"javascript" : "js",
		"python" : "py",
		"c++" : "cpp",
		"c" : "c",
		"java" : "java",
		'html' : 'html'
	}

	moss_obj.addFilesByWildcard(testfiles_path+"/*."+language_extensions[language])

	url = moss_obj.send()
	print ("Report Url: " + url)

	mosspy.download_report(url, report_path+"/report", connections = 8)


def main():
	if len(sys.argv) <  6:
		if len(sys.argv) == 1 and sys.argv[1] == '--help':
			print("To run a moss test use:\n\'python moss.py <userid> <language> <basefile name> <testfiles directory path> <report directory>\'\nTestfiles must all be in the same directory!\nReport is generated in a directory called \'report\'\n")
		else:
			print('Too few arguments!\nFormat is \'python moss.py <userid> <language> <basefile name> <testfiles directory path> <report directory>\'\nType \'python moss.py --help\' to get help\' or read README.md')	
		sys.exit(0)
	else:
		get_moss_results(userid = sys.argv[1], language = sys.argv[2], basefile_name = sys.argv[3], testfiles_path = sys.argv[4], report_path = sys.argv[5])

if __name__ == '__main__':
	main()

