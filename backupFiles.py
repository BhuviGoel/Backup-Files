import os
import shutil
import time

def main():
	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = input("Enter the path of files/folder you want to delete: ")

	# converting days to seconds
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			# comparing the days
			if seconds >= get_file_or_folder_age(root_folder):

				# remove_folder function
				remove_folder(root_folder)
				deleted_folders_count += 1 

			else:
				for folder in folders:
					# folder path
					folder_path = os.path.join(root_folder, folder)
					# comparing with the days
					if seconds >= get_file_or_folder_age(folder_path):
						# remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1

				for f in files:
					# file path
					file_path = os.path.join(root_folder, f)
					# comparing the days
					if seconds >= get_file_or_folder_age(file_path):
						# remove_file function
						remove_file(file_path)
						deleted_files_count += 1
		else:
			# if the path is not a directory
			if seconds >= get_file_or_folder_age(path):

				remove_file(path)
				deleted_files_count += 1
	else:
		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):
	# removing the folder
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"Unable to delete the "+path)

def remove_file(path):
	# removing the file
	if not os.remove(path):
		print(f"{path} is removed successfully")
	else:
		print("Unable to delete the "+path)

def get_file_or_folder_age(path):
	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	return ctime

main()