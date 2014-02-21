
 #################### SGOMS EOC Model ###################



import sys
sys.path.append('/Users/robertwest/CCMSuite-old')

import ccm      
log=ccm.log()
#log=ccm.log(html=True) 

from ccm.lib.actr import *



# --------------- Environment ------------------

class MyEnvironment(ccm.Model):
    
## buildings
    
    substation1=ccm.Model(isa='building',location='town',state='good')
    substation2=ccm.Model(isa='building',location='town',state='good')
    hospital=ccm.Model(isa='building',location='town',state='good')
    areana=ccm.Model(isa='building',location='town',state='good')
    housing=ccm.Model(isa='building',location='town',state='good')

## vehicles

    ambulance=ccm.Model(isa='vehicle',location='town',state='good')
    policecar=ccm.Model(isa='vehicle',location='town',state='good')
    firetruck=ccm.Model(isa='vehicle',location='town',state='good')
    socialworkers=ccm.Model(isa='vehicle',location='town',state='good')

## EOC

    informationboard=ccm.Model(isa='info_board',message='none')
    clock=ccm.Model('time:0')


class MotorModule(ccm.Model):     ### defines actions on the environment
        
    def change(self, env_object, slot_value):
        #yield 2                   
        x = eval('self.parent.parent.' + env_object)
        x.time= slot_value
        print env_object
        print slot_value
        print 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
        
        
# --------------- Clock Management Agent ------------------

class C_Agent(ACTR):

    production_time=0.05

    countbuffer=Buffer()
    b_motor=Buffer()
    motor=MotorModule(b_motor)

    def init():                                             
        countbuffer.set('0 run')

    def advance_clock(countbuffer='?count run'):
        b=int(count)
        c=b+1
        a=str(c)
        countbuffer.set(a+' update')
        print a
        print 'fffffffffffffffffffffffffffffffffffffffffffffff'

    def change(countbuffer='?count update'):
        motor.change('clock',count)
        countbuffer.set('?count run')


# --------------- Environment Management Agent ------------------

class E_Agent(ACTR):

    production_time=0.05

    countbuffer=Buffer()
    b_motor=Buffer()
    motor=MotorModule(b_motor)


    def event1(clock='time:3'):
        print 'fire'
        print 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'










############## run model ###########################
####################################################
          
tim=C_Agent()                              # name the agent
tom=E_Agent() 
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
subway.agent=tom
ccm.log_everything(subway)                 # print out what happens in the environment

subway.run()                               # run the environment
ccm.finished()                             # stop the environment
