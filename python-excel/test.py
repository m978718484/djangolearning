#coding=utf-8
import xlrd,pyExcelerator
import os
path='in'#文件夹名
def print_xls(path):
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
    #print start_point
    #print end_point        
    start_length = len(start_point)
    end_length = len(end_point)
    if start_length != end_length:
        print 'error format excel'
    else:
        wb = pyExcelerator.Workbook()

        ws = wb.add_sheet(u'客流量')
        ws.write(0,0,u'车次')
        ws.write(0,1,u'始发时间')
        ws.write(0,2,u'到站时间')
        ws.write(0,3,u'开车时间')
        ws.write(0,4,u'上车人数')
        ws.write(0,5,u'下车人数')
        ws.write(0,6,u'站点名称')

        time = table.cell(1,0).value.encode('utf-8').split()
        train = ''
        ws_r_index = 1
        ws_r_index1 = 1
        k01 = ''
        for i in range(start_length):
            for r in range(start_point[i][0]+2,end_point[i][0]):
                ws_c_index = 0
                 #车次
                train = table.cell(start_point[i][0]-1,0).value.encode('utf-8')
                if train.split()[0] == 'K01':
                    k01 = train
                ws.write(ws_r_index,0,train.split()[0])

                #始发日期
                ws.write(ws_r_index,1,time[1].split(r'—')[0] )
               
                #到站时间
                arrived_time = table.cell(r,1).value
                ws.write(ws_r_index,2,arrived_time if arrived_time is not None and arrived_time != '' else 'N/A')

                #下车人数
                down_count = table.cell(r,start_point[i][1]).value
                ws.write(ws_r_index,5,down_count if down_count is not None and down_count != '' else 0)

                #下车站点
                ws.write(ws_r_index,6,table.cell(r,0).value)
                
                
                ws_r_index += 1



            for r_up in range(end_point[i][1]+2,start_point[i][1]):

                #开车时间
                leaved_time = table.cell(start_point[i][0]+1,r_up).value
                ws.write(ws_r_index1,3,leaved_time if leaved_time is not None and leaved_time != '' else 'N/A')

                #上车人数
                up_count = table.cell(end_point[i][0],r_up).value
                ws.write(ws_r_index1,4,up_count if up_count is not None and up_count != '' else 0)
                if k01 != '':
                    print leaved_time,up_count
                ws_r_index1 += 1

        wb.save(path.replace('in','out'))
           
                        
if __name__=='__main__':
    for root, dirs, files in os.walk( path ):
        for fn in files:
            print_xls( '%s\\%s'%(root,fn))
