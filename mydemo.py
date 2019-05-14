import sys
import os
import json
import random
sys.path.append('./src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter
import glob


def writeHTML(video_ls, output_folder_name, genre):

	length = len(video_ls)
	t = Table()
	print('length : ', length)
	for r in range(length):
		count = r
		if r == 0:
			r = TableRow(isHeader = True)
			a1 = Element()
			a1.addTxt("No.")
			r.addElement(a1)
			a2 = Element()
			a2.addTxt("Viedo_ID")
			r.addElement(a2)
			a3 = Element()
			a3.addTxt("Genre")
			r.addElement(a3)

			a4 = Element()
			a4.addTxt("Handscore")
			r.addElement(a4)	

			a4 = Element()
			a4.addTxt("Is_beauty")
			r.addElement(a4)	

			a4 = Element()
			a4.addTxt("Is_cartoon")
			r.addElement(a4)		

			a5 = Element()
			a5.addTxt("Thumbnail_1")
			r.addElement(a5)
			a6 = Element()
			a6.addTxt("Thumbnail_2")
			r.addElement(a6)
			a7 = Element()
			a7.addTxt("Thumbnail_3")
			r.addElement(a7)
			a8 = Element()
			a8.addTxt("Thumbnail_4")
			r.addElement(a8)
			a9 = Element()
			a9.addTxt("Link")
			r.addElement(a9)

			t.addRow(r)
			continue
		else:
			r = TableRow()
		# print(count)
		# print(v_id[count-1])
		# print(label_json[v_id[count-1]])
		# print(genre[str(label_json[v_id[count-1]]) ])


		a = Element()	# no.
		a.addTxt("No." + str(count))
		r.addElement(a)
		b = Element()	# video id
		b.addTxt(video_ls[count-1][0])
		r.addElement(b)
		c = Element()	# genre
		c.addTxt(genre)
		r.addElement(c)

		c = Element()	# score
		c.addTxt(video_ls[count-1][1])
		r.addElement(c)

		c = Element()	# score
		c.addTxt(video_ls[count-1][2])
		r.addElement(c)

		c = Element()	# score
		c.addTxt(video_ls[count-1][0])
		r.addElement(c)
		

		for i in range(4):	# 4 thumbnails
			f = Element()
			f.addImg("https://img.youtube.com/vi/" + video_ls[count-1][0] + "/" + str(i) +".jpg")      
			r.addElement(f)
		g = Element("click me")	# link
		g.addLink("https://www.youtube.com/watch?v=" + video_ls[count-1][0])
		r.addElement(g)

		t.addRow(r)
	tw = TableWriter(t, output_folder_name)
	tw.write()



txt_folder_path = "."
txt_file_list = glob.glob("./beauty_picked.txt")
print(txt_file_list)
#txt_file_list = ["beauty_sorted_by_handscore.txt"]
for txt_file_path in txt_file_list:
	#txt_file_path = os.path.join(txt_folder_path, txt_file_name)
	#
	output_folder_name = txt_file_path.split("/")[-1][:-4]
	genre = output_folder_name.split("_")[0]
	#
	video_ls = []

	with open(txt_file_path, "r") as f:
		for item in f:
			item = item.strip()
			video_id, handscore, is_beauty= item.split(" ")

			video_ls.append( [video_id, handscore, is_beauty] )





	writeHTML(video_ls, output_folder_name, genre)


