#coding=utf-8
import xlrd,pyExcelerator
import os,re
import sqlite3

path='in'#文件夹名
db_path = 'test.db'


def print_xls(path,leave_date):
    data = xlrd.open_workbook(path)   
    table=data.sheets()[0]#打开excel的第几个sheet
    start_point = []
    end_point = []
     
    for r in xrange(table.nrows):
        for c in xrange(table.ncols):
            value = table.cell(r,c).value
            if value == u'下车人数合计':
                start_point.append((r,c))
            if value ==u'上车人数合计':
                end_point.append((r,c))


    start_length = len(start_point)
    end_length = len(end_point)

    if start_length != end_length:
        print 'error format excel'
    else:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        wb = pyExcelerator.Workbook()
        ws = wb.add_sheet(u'train')
        ws.write(0,0,u'始发日期')
        ws.write(0,1,u'车次')
        ws.write(0,2,u'站点')
        ws.write(0,3,u'到站时间')
        ws.write(0,4,u'下车人数')
        ws.write(0,5,u'开车时间')
        ws.write(0,6,u'上车人数')

        begin_insert = 0
        ws_r = 1 
        for i in range(start_length):
            for r in range(start_point[i][0]+2,end_point[i][0]):
                down_site = table.cell(r,0).value
                train = table.cell(start_point[i][0]-1,0).value.encode('utf-8')
                train = train.split()[0]
                arrived_time = table.cell(r,1).value
                patterns_train = re.compile(r'ZD111-\d+')
                match = patterns_train.match( down_site )
                if match:
                    begin_insert = 1
                down_count = table.cell(r,start_point[i][1]).value
                for r_up in range(end_point[i][1]+2,start_point[i][1]):
                    up_site = table.cell(start_point[i][0],r_up).value
                    leave_time = table.cell(start_point[i][0] + 1,r_up).value
                    up_count = table.cell(end_point[i][0],r_up).value
                    if down_site == up_site and begin_insert:
                        #print leave_date,train,up_site,arrived_time,down_count,leave_time,up_count
                        ws.write(ws_r,0,leave_date)
                        ws.write(ws_r,1,train)
                        ws.write(ws_r,2,up_site)
                        ws.write(ws_r,3,arrived_time)
                        ws.write(ws_r,4,down_count)
                        ws.write(ws_r,5,leave_time)
                        ws.write(ws_r,6,up_count)
                        ws_r += 1

                        #cursor.execute("insert into railway values (?,?,?,?,?,?,?)",(leave_date,train,up_site,arrived_time,down_count,leave_time,up_count))
                        break
                if r + 1 == end_point[i][0]:
                    ws.write(ws_r,0,leave_date)
                    ws.write(ws_r,1,train)
                    ws.write(ws_r,2,down_site)
                    ws.write(ws_r,3,arrived_time)
                    ws.write(ws_r,4,down_count)
                    ws.write(ws_r,5,'N/A')
                    ws.write(ws_r,6,0)
                    ws_r += 1

                    #print leave_date,train,down_site,arrived_time,down_count,'N/A',0
                    #cursor.execute("insert into railway values (?,?,?,?,?,?,?)",(leave_date,train,down_site,arrived_time,down_count,'N/A',0))
                    break
            begin_insert = 0

        wb.save(path.replace('in\\','out\\out'))
        conn.commit()
        cursor.close()
        conn.close()  

if __name__=='__main__':
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE "railway" ("leave_date" VARCHAR(20), "train" VARCHAR(20), "site" VARCHAR(20), "arrived_time" VARCHAR(10), "down_count" INTEGER, "leaved_time" VARCHAR(10), "up_count" INTEGER)')
        conn.commit()
        cursor.close()
        conn.close()

    for root, dirs, files in os.walk( path ):
        for fn in files:

            print_xls( '%s\\%s'%(root,fn),fn.replace('.xls','') )