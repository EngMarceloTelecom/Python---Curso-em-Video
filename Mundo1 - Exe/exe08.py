d = float(input('Distância em Metros: '))
km = d/1000
Hm = d/100
dam = d/10
dm = d*10
cm = d*100
mm = d*1000

print ('{:.4f} km, {:.4f} hm, {:.4f} dam, {} dm, {} cm, {} mm,'.format(km,Hm,dam,dm,cm,mm))
