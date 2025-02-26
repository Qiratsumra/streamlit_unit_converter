import streamlit as st

# page config
st.set_page_config(page_title='Unit Converter',page_icon='🔢')

st.title('Unit Converter')
st.caption('Welcome to the Unit Converter!')

# Enter the value to be converted
value = st.number_input('Enter the value to be converted')

option1= st.selectbox('Select the unit to convert from',('Kilometer','Meter','Centimeter','Millimeter','Micrometer','Nanometer','Mile','Yard','Foot','Inch','Nautical Mile'))
option2= st.selectbox('Select the unit to convert to',('Kilometer','Meter','Centimeter','Millimeter','Micrometer','Nanometer','Mile','Yard','Foot','Inch','Nautical Mile'))

if st.button('Convert') and st.balloons():
    # for Kiliometer
    if option1 =='Kilometer' and option2 == 'Kilometer':
        st.success(f'{value}km')
    elif option1 =='Kilometer' and option2 == 'Meter':
     st.success(f'{value*1000}m')
    elif option1 =='Kilometer' and option2 == 'Centimeter':
       st.success(f'{value*100000}cm')
    elif option1 =='Kilometer' and option2 == 'Millimeter':
       st.success(f'{value*1000000}mm')
    elif option1 =='Kilometer' and option2 == 'Micrometer':
       st.success(f"{value*1000000000}μm")
    elif  option1 =='Kilometer' and option2 == 'Nanometer':
       st.success(f'{value*1000000000000}nm')
    elif option1 =='Kilometer' and option2 == 'Mile':
       st.success(f"{value*0.621371}mi")
    elif option1 =='Kilometer' and option2 == 'Yard':
       st.success(f'{value*1093.61}yd')
    elif option1 =='Kilometer' and option2 == 'Foot':
       st.success(f'{value*3280.84}ft')
    elif option1 =='Kilometer' and option2 == 'Inch':
       st.success(f'{value*39370.1}in')
    elif option1 =='Kilometer' and option2 == 'Nautical Mile':
         st.success(f'{value*0.539957}nmi')
    
    # Meter
    elif option1 =='Meter' and option2 == 'Kilometer':
        st.success(f'{value/1000}km')
    elif option1 =='Meter' and option2 == 'Meter':
        st.success(f'{value}m')
    elif option1 =='Meter' and option2 == 'Centimeter':
        st.success(f'{value*100}cm')
    elif option1 =='Meter' and option2 == 'Millimeter':
        st.success(f'{value*1000}mm')
    elif option1 =='Meter' and option2 == 'Micrometer': 
        st.success(f'{value*1000000}μm')
    elif option1 =='Meter' and option2 == 'Nanometer':
        st.success(f'{value*1000000000}nm')
    elif option1 =='Meter' and option2 == 'Mile':
        st.success(f'{value*0.000621371}mi')
    elif option1 =='Meter' and option2 == 'Yard':    
        st.success(f'{value*1.09361}yd')
    elif option1 =='Meter' and option2 == 'Foot':
        st.success(f'{value*3.28084}ft')
    elif option1 =='Meter' and option2 == 'Inch':
        st.success(f"{value*39.3701}in")
    elif option1 =='Meter' and option2 == 'Nautical Mile':
        st.success(f'{value*0.000539957}nmi') 
    
    # Centimeter
    elif option1 =='Centimeter' and option2 == 'Kilometer':
        st.success(f'{value/100000}km')
    elif option1 =='Centimeter' and option2 == 'Meter':
        st.success(f'{value/100}m')
    elif option1 =='Centimeter' and option2 == 'Centimeter':
        st.success(f'{value}cm')
    elif option1 =='Centimeter' and option2 == 'Millimeter':
        st.success(f'{value*10}mm')
    elif option1 =='Centimeter' and option2 == 'Micrometer':
        st.success(f"{value*10000}μm")
    elif option1 =='Centimeter' and option2 == 'Nanometer':
        st.success(f"{value*10000000}nm")
    elif option1 =='Centimeter' and option2 == 'Mile':
        st.success(f"{value*0.0000062137}mi")
    elif option1 =='Centimeter' and option2 == 'Yard':
        st.success(f'{value*0.0109361}yd')
    elif option1 =='Centimeter' and option2 == 'Foot':
        st.success(f"{value*0.0328084}ft")
    elif option1 =='Centimeter' and option2 == 'Inch':
        st.success(f"{value*0.393701}in")
    elif option1 =='Centimeter' and option2 == 'Nautical Mile':
        st.success(f'{value*0.00000539957}nmi')

    # Millimeter
    elif option1 =='Millimeter' and option2 == 'Kilometer':
        st.success(f'{value/1000000}km')
    elif option1 =='Millimeter' and option2 == 'Meter':
        st.success(f'{value/1000}m')
    elif option1 =='Millimeter' and option2 == 'Centimeter':
        st.success(f'{value/10}cm')
    elif option1 =='Millimeter' and option2 == 'Millimeter':
        st.success(f'{value}mm')
    elif option1 =='Millimeter' and option2 == 'Micrometer':
        st.success(f'{value*1000}μm')
    elif option1 =='Millimeter' and option2 == 'Nanometer':
        st.success(f'{value*1000000}nm')
    elif option1 =='Millimeter' and option2 == 'Mile':
        st.success(f'{value*0.00000062137}mi')
    elif option1 =='Millimeter' and option2 == 'Yard':
        st.success(f'{value*0.00109361}yd')
    elif option1 =='Millimeter' and option2 == 'Foot':
        st.success(f'{value*0.00328084}ft')
    elif option1 =='Millimeter' and option2 == 'Inch':
        st.success(f'{value*0.0393701}in')
    elif option1 =='Millimeter' and option2 == 'Nautical Mile':
        st.success(f'{value*0.000000539957}nmi')

    # Micrometer
    elif option1 =='Micrometer' and option2 == 'Kilometer':
        st.success(f'{value/1000000000}km')
    elif option1 =='Micrometer' and option2 == 'Meter':
        st.success(f'{value/1000000}m')
    elif option1 =='Micrometer' and option2 == 'Centimeter':
        st.success(f'{value/10000}cm')
    elif option1 =='Micrometer' and option2 == 'Millimeter':
        st.success(f'{value/1000}mm')
    elif option1 =='Micrometer' and option2 == 'Micrometer':
        st.success(f'{value}μm')
    elif option1 =='Micrometer' and option2 == 'Nanometer':
        st.success(f'{value*1000}nm')
    elif option1 =='Micrometer' and option2 == 'Mile':
        st.success(f'{value*0.00000000062137}mi')
    elif option1 =='Micrometer' and option2 == 'Yard':
        st.success(f'{value*0.00000109361}yd')
    elif option1 =='Micrometer' and option2 == 'Foot':
        st.success(f'{value*0.00000328084}ft')
    elif option1 =='Micrometer' and option2 == 'Inch':
        st.success(f'{value*0.0000393701}in')
    elif option1 =='Micrometer' and option2 == 'Nautical Mile':
        st.success(f'{value*0.000000000539957}nmi')
    
    # Nanometer
    elif option1 =='Nanometer' and option2 == 'Kilometer':
        st.success(f'{value/1000000000000}km')
    elif option1 =='Nanometer' and option2 == 'Meter':
        st.success(f'{value/1000000000}m')
    elif option1 =='Nanometer' and option2 == 'Centimeter':
        st.success(f'{value/10000000}cm')
    elif option1 =='Nanometer' and option2 == 'Millimeter':
        st.success(f'{value/1000000}mm')
    elif option1 =='Nanometer' and option2 == 'Micrometer':
        st.success(f'{value/1000}μm')
    elif option1 =='Nanometer' and option2 == 'Nanometer':
        st.success(f'{value}nm')
    elif option1 =='Nanometer' and option2 == 'Mile':
        st.success(f'{value*0.00000000000062137}mi')
    elif option1 =='Nanometer' and option2 == 'Yard':
        st.success(f'{value*0.00000000109361}yd')
    elif option1 =='Nanometer' and option2 == 'Foot':
        st.success(f'{value*0.00000000328084}ft')
    elif option1 =='Nanometer' and option2 == 'Inch':
        st.success(f'{value*0.0000000393701}in')
    elif option1 =='Nanometer' and option2 == 'Nautical Mile':
        st.success(f'{value*0.000000000000539957}nmi')

    # Mile
    elif option1 =='Mile' and option2 == 'Kilometer':
        st.success(f'{value/0.621371}km')
    elif option1 =='Mile' and option2 == 'Meter':
        st.success(f'{value/0.000621371}m')
    elif option1 =='Mile' and option2 == 'Centimeter':
        st.success(f'{value/0.0000062137}cm')
    elif option1 =='Mile' and option2 == 'Millimeter':
        st.success(f'{value/0.00000062137}mm')
    elif option1 =='Mile' and option2 == 'Micrometer':
        st.success(f'{value/0.00000000062137}μm')
    elif option1 =='Mile' and option2 == 'Nanometer':
        st.success(f'{value/0.00000000000062137}nm')
    elif option1 =='Mile' and option2 == 'Mile':
        st.success(f'{value}mi')
    elif option1 =='Mile' and option2 == 'Yard':
        st.success(f'{value*1760}yd')
    elif option1 =='Mile' and option2 == 'Foot':
        st.success(f'{value*5280}ft')
    elif option1 =='Mile' and option2 == 'Inch':
        st.success(f'{value*63360}in')
    elif option1 =='Mile' and option2 == 'Nautical Mile':
        st.success(f'{value*0.868976}nmi')
    
    # Yard
    elif option1 =='Yard' and option2 == 'Kilometer':
        st.success(f'{value/1093.61}km')
    elif option1 =='Yard' and option2 == 'Meter':
        st.success(f'{value/1.09361}m')
    elif option1 =='Yard' and option2 == 'Centimeter':
        st.success(f'{value/0.0109361}cm')
    elif option1 =='Yard' and option2 == 'Millimeter':
        st.success(f'{value/0.00109361}mm')
    elif option1 =='Yard' and option2 == 'Micrometer':
        st.success(f'{value/0.00000109361}μm')
    elif option1 =='Yard' and option2 == 'Nanometer':
        st.success(f'{value/0.00000000109361}nm')
    elif option1 =='Yard' and option2 == 'Mile':
        st.success(f'{value/1760}mi')
    elif option1 =='Yard' and option2 == 'Yard':
        st.success(f'{value}yd')
    elif option1 =='Yard' and option2 == 'Foot':
        st.success(f'{value*3}ft')
    elif option1 =='Yard' and option2 == 'Inch':
        st.success(f'{value*36}in')
    elif option1 =='Yard' and option2 == 'Nautical Mile':
        st.success(f'{value*0.000568182}nmi')

    # Foot
    elif option1 =='Foot' and option2 == 'Kilometer':
        st.success(f'{value/3280.84}km')
    elif option1 =='Foot' and option2 == 'Meter':
        st.success(f'{value/3.28084}m')
    elif option1 =='Foot' and option2 == 'Centimeter':
        st.success(f'{value/0.0328084}cm')
    elif option1 =='Foot' and option2 == 'Millimeter':
        st.success(f'{value/0.00328084}mm')
    elif option1 =='Foot' and option2 == 'Micrometer':
        st.success(f'{value/0.00000328084}μm')
    elif option1 =='Foot' and option2 == 'Nanometer':
        st.success(f'{value/0.00000000328084}nm')
    elif option1 =='Foot' and option2 == 'Mile':
        st.success(f'{value/5280}mi')
    elif option1 =='Foot' and option2 == 'Yard':
        st.success(f'{value/3}yd')
    elif option1 =='Foot' and option2 == 'Foot':
        st.success(f'{value}ft')
    elif option1 =='Foot' and option2 == 'Inch':
        st.success(f'{value*12}in')
    elif option1 =='Foot' and option2 == 'Nautical Mile':
        st.success(f'{value*0.000164579}nmi')

    # Inch
    elif option1 =='Inch' and option2 == 'Kilometer':
        st.success(f'{value/39370.1}km')
    elif option1 =='Inch' and option2 == 'Meter':
        st.success(f'{value/39.3701}m')
    elif option1 =='Inch' and option2 == 'Centimeter':
        st.success(f'{value/0.393701}cm')
    elif option1 =='Inch' and option2 == 'Millimeter':
        st.success(f'{value/0.0393701}mm')
    elif option1 =='Inch' and option2 == 'Micrometer':
        st.success(f'{value/0.0000393701}μm')
    elif option1 =='Inch' and option2 == 'Nanometer':
        st.success(f'{value/0.0000000393701}nm')
    elif option1 =='Inch' and option2 == 'Mile':
        st.success(f'{value/63360}mi')
    elif option1 =='Inch' and option2 == 'Yard':
        st.success(f'{value/36}yd')
    elif option1 =='Inch' and option2 == 'Foot':
        st.success(f'{value/12}ft')
    elif option1 =='Inch' and option2 == 'Inch':
        st.success(f'{value}in')
    elif option1 =='Inch' and option2 == 'Nautical Mile':
        st.success(f'{value*0.0000137158}nmi')

    # Nautical Mile
    elif option1 =='Nautical Mile' and option2 == 'Kilometer':
        st.success(f'{value/0.539957}km')
    elif option1 =='Nautical Mile' and option2 == 'Meter':  
        st.success(f'{value/0.000539957}m')
    elif option1 =='Nautical Mile' and option2 == 'Centimeter':
        st.success(f'{value/0.00000539957}cm')
    elif option1 =='Nautical Mile' and option2 == 'Millimeter':
        st.success(f'{value/0.000000539957}mm')
    elif option1 =='Nautical Mile' and option2 == 'Micrometer':
        st.success(f'{value/0.000000000539957}μm')
    elif option1 =='Nautical Mile' and option2 == 'Nanometer':
        st.success(f'{value/0.000000000000539957}nm')
    elif option1 =='Nautical Mile' and option2 == 'Mile':
        st.success(f'{value/0.868976}mi')
    elif option1 =='Nautical Mile' and option2 == 'Yard':
        st.success(f'{value/0.000568182}yd')
    elif option1 =='Nautical Mile' and option2 == 'Foot':
        st.success(f'{value/0.000164579}ft')
    elif option1 =='Nautical Mile' and option2 == 'Inch':
        st.success(f'{value/0.0000137158}in')
    elif option1 =='Nautical Mile' and option2 == 'Nautical Mile':
        st.success(f'{value}nmi')
    else:
        st.error('Please select the units to convert')



st.write('-------------------------------------------------')
st.caption('©️ 2025 Unit Converter By Qirat Saeed. All rights reserved.')   
