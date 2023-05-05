import pandas as pd 

												

def link2007() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link2007'].values.tolist())

def  link_09() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df[' link_09'].values.tolist())

def link2008() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link2008'].values.tolist())

def   link_10() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link10'].values.tolist())

def link_11() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link11'].values.tolist())

def link_12() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link12'].values.tolist())

def link_13() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link13'].values.tolist())

def link_14() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link14'].values.tolist())

def link_15() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link15'].values.tolist())

def link_16() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link16'].values.tolist())

def link_17() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link17'].values.tolist())

def link_18() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link18'].values.tolist())

def link_19() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link19'].values.tolist())

def link_20() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link20'].values.tolist())

def link_21() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link21'].values.tolist())

def link_22() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link22'].values.tolist())

def link_23() :
    df = pd.read_csv('/home/abdo/forex/links.csv')
    return (df['link23'].values.tolist())


y = 2023


for m in ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']:
    if m == 'jan' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')

    if m == 'feb' :
            for d in range (1,29) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')

    if m == 'mar' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
        
    if m == 'apr' :
            for d in range (1,31) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')

    if m == 'may' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'jun' :
            for d in range (1,31) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'jul' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'aug' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'sep' :
            for d in range (1,31) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'oct' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'nov' :
            for d in range (1,31) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
    if m == 'dec' :
            for d in range (1,32) :
                print(f'https://www.forexfactory.com/calendar?day={m}{d}.{y}')
