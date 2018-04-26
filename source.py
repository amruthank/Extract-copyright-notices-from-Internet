#Function to capture all the copyright notice from the license file

tag = Html tags!!
copy_right = None
copyright_list = [] 
is_copyright = False


def capture_copyright(tag, copy_right, copyright_list, is_copyright):

    re_copyright = re.compile(r'copyright (\([Cc@]\)|\d+).*', re.IGNORECASE)
    re_junk_copyright = re.compile('copyright.*\<YEAR\>.*', re.IGNORECASE)

    if re_junk_copyright.search(tag.text) != None:
        return ("", copyright_list, False)
        
    if tag.text != " ":
        
        found_copyright_notice = re_copyright.search(tag.text)
    
        if found_copyright_notice != None and found_copyright_notice.group(0) not in copyright_list: #Re-test for multiple copyrights in the license file.
                            
            if len(tag.text) > 100: #If the copyright and license texts are text?!
                is_lengthy_text = True
                lengthy_text = tag.text

                for line in lengthy_text.split("\n"):
                    copyright_notice_from_lengthy_text = re_copyright.search(line)
                    if copyright_notice_from_lengthy_text != None:
                        copy_right = copyright_notice_from_lengthy_text.group(0)
                            
            elif len(tag.text) > 30 and not (re_copyright.search(found_copyright_notice.group(0))): #For the plain copyright text from the license.
                copy_right = ""
            else:            
                copy_right = found_copyright_notice.group(0)
            
            #if tag.text not in copyright_list and tag.text not in ["Copyright","copyright"]:
            if copy_right != "" and re.sub('All Rights Reserved.',"", copy_right, flags=re.IGNORECASE) not in copyright_list:
                copyright_list.append(re.sub('All Rights Reserved.',"", copy_right, flags=re.IGNORECASE))
                
            is_copyright = True
                
    return (copy_right, copyright_list, is_copyright)
#End of the function capture_copyright function.  
