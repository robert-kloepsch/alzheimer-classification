import os
import shutil
import glob

destinationpath = './data/OASIS/3D/'
print(os.getcwd())
def get_folders(sourcepath):
    sessionfolder = os.listdir(sourcepath)
    files = [folder.split('_')[1] for folder in sessionfolder]
    return files
files = get_folders('./data/OASIS/ALL/')

missing_files = []
for file in files:
    sourcepath = './data/OASIS/ALL/OAS1_' + file + '_MR1/PROCESSED/MPRAGE/T88_111/'
    file_end_img = glob.glob(sourcepath+ 'OAS1_' + file + '_MR1_mpr_n*_anon_111_t88_masked_gfc.img')
    file_end_hdr = glob.glob(sourcepath+ 'OAS1_' + file + '_MR1_mpr_n*_anon_111_t88_masked_gfc.hdr')
    print(file_end_img)
    print(os.path.join(destinationpath, 'OAS1_' + file + '_MR1_mpr_n*_anon_111_t88_masked_gfc.img'))
    if len(file_end_img)>0: 
        shutil.copy(file_end_img[0], os.path.join(destinationpath, 'OAS1_' + file + '.img'))
    if len(file_end_hdr)>0: 
        shutil.copy(file_end_hdr[0], os.path.join(destinationpath, 'OAS1_' + file + '.hdr'))

    else: 
        missing_files.append(file)
print(missing_files)

# missing files ['0303', '0317', '0101', '0115', '0129', '0368', '0075', '0061', '0049', '0288', '0156', '0277', '0263', '0262', '0289', '0060', '0074', '0114', '0316', '0302', '0314', '0300', '0328', 'Store', '0001', '0013', '0101', '0156', '0368', '0061']
# verify