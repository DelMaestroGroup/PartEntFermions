// POV-Ray 3.7 Scene File "antiperiodicBC.pov"
// Inspired by http://www.f-lohmueller.de/pov_tut/loop/povlup3e.htm
// for making moebius strips
//--------------------------------------------------------------------------
#version 3.7;
global_settings{ assumed_gamma 1.0 }
#default{ finish{ ambient 0.1 diffuse 0.9 }} 
//--------------------------------------------------------------------------
#include "colors.inc"
#include "textures.inc"
#include "glass.inc"
#include "metals.inc"
#include "golds.inc"
#include "stones.inc"
#include "woods.inc"
#include "shapes.inc"
#include "shapes2.inc"
#include "functions.inc"
#include "math.inc"
#include "transforms.inc"

//---------------------------------------------------------------------------------
//---------------------------------------------------------------------------------
#declare Camera_Number = 4 ;
//---------------------------------------------------------------------------------
// camera -------------------------------------------------------------------------
#switch ( Camera_Number )
#case (0)
  #declare Camera_Location = < 0.00, 1.00,-13.00> ;  // front view
  #declare Camera_Look_At  = < 0.00, 1.00 , 0.0> ;
  #declare Camera_Angle    =  45 ;
#break
#case (1)
  #declare Camera_Location =  < 5.00, 6.00,-8.00> ;  // diagonal view
  #declare Camera_Look_At  =  < 0.9 , 0.3 ,  0.0>;
  #declare Camera_Angle    =  50 ;
#break
#case (2)
  #declare Camera_Location = <10.00, 1.00,  0.00> ;  // right side view
  #declare Camera_Look_At  = < 0.00, 1.00,  0.00> ;
  #declare Camera_Angle    =  50 ;
#break
#case (3)
  #declare Camera_Location = < 0.00,12.00,  0+0.000> ;  // top view
  #declare Camera_Look_At  = < 0.00, 0.00,  0+0.001> ;
  #declare Camera_Angle    = 50 ;
#break
#case (4)
  #declare Camera_Location = < 0.00, 4.00,  -18.5> ;  // top view
  #declare Camera_Look_At  = < 0.00, 0.00,  0> ;
  #declare Camera_Angle    = 45;
#break
#else
  #declare Camera_Location = < 0.00, 1.00,-13.00> ;  // front view
  #declare Camera_Look_At  = < 0.00, 1.00 , 0.0> ;
  #declare Camera_Angle    =  45 ;
#break
#break
#end // of "#switch ( Camera_Number )"  
//--------------------------------------------------------------------------
camera{ ultra_wide_angle // orthographic 
        location Camera_Location
        right    x*image_width/image_height
        angle    Camera_Angle
        look_at  Camera_Look_At
      }
//--------------------------------------------------------------------------
// sun ---------------------------------------------------------------------
//--------------------------------------------------------------------------
light_source{< 1800,2500, -2500> color rgb<1,1,1>*0.9}                // sun 
light_source{ Camera_Location   color rgb<0.9,0.9,1>*0.1 shadowless} // flash

//----------------------------------------------------------------------------
//---------------------------- objects in scene ------------------------------
//----------------------------------------------------------------------------
#declare Ball = 
sphere{ <0,0,0>,0.50
  texture
  {
   pigment{ color rgb<0.255,0.451,0.702> }
    normal {bozo 0.05 scale 0.1}
    finish{
         diffuse 0.65
         brilliance 0.6
         reflection{
                rgb <.05, .05, .05>, rgb<.2,.2,.2>
                fresnel on       
         }
    }

  }
}

#declare Ball2 =
 sphere{ <0,0,0>,0.50
  texture
  {
    pigment{ color rgb<0.49,0.796,0.643> } // green
    normal {bozo 0.05 scale 0.1}
    finish{
         diffuse 0.65
         brilliance 0.6
         reflection{
                rgb <.05, .05, .05>, rgb<.2,.2,.2>
                fresnel on       
         }
    }

  }
}
 

//----------------------------------------------------------------------
//----------------------------------------------------------------------
#declare Profile_R = 0.02;
#declare Profile_H = 0.50;

#declare Profile = 
union{
 sphere  {<0,0,0>,Profile_R  translate<0, Profile_H,0>}
 cylinder{<0,-Profile_H,0>,<0, Profile_H,0>,Profile_R }
 sphere  {<0,0,0>,Profile_R  translate<0,-Profile_H,0>}
 texture{ pigment{ color rgb<0.60,0.60,0.60> transmit 0.82}
          finish { phong 1}}}


//---------------------------------------------------------
#declare R_major = 3.00;
#declare N_major = 0.5; 
#declare N_minor = 2880;


// Periodic Boundary Conditions -----------------------------------
#declare PBC =
union {
#declare factor= 0;

//---------------------------------------------------------
#declare Nr = 0;                  // start
#declare EndNr = N_major*N_minor; // end

#while (Nr< EndNr)                // loop 
 object{Profile
         rotate<0,0,factor * Nr * 360/N_minor>
         translate<R_major,0,0> 
         rotate<0, Nr * 360/EndNr,0>
       } //------------------------

#declare Nr = Nr + 1;  // next Nr
#end // --------------------------// end of loop

#declare R = 3.00;
#declare Nr = 0;      // start
#declare EndNr = 7;  // end

// the particles

// #1 
object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

// #2 
object{ Ball2
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

// #3 
object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

// #4 
object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

// #5 
object{ Ball2
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

// #6 
object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

// #7 
object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;
}

// Anti Periodic Boundary Conditions ----------------------
#declare APBC =
union {

#declare factor= 1;

//---------------------------------------------------------
#declare Nr = 0;                  // start
#declare EndNr = N_major*N_minor; // end

#while (Nr< EndNr)                // loop 
 object{Profile
         rotate<0,0,factor * Nr * 360/N_minor>
         translate<R_major,0,0> 
         rotate<0, Nr * 360/EndNr,0>
       } //------------------------

#declare Nr = Nr + 1;  // next Nr
#end // --------------------------// end of loop

#declare R = 3.00;

// the particles
#declare Nr = 0;      // start
#declare EndNr = 8;  // end

object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr + 1;  // next Nr

object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr + 1;  // next Nr

object{ Ball2
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr + 1;  // next Nr

object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr + 1;  // next Nr

object{ Ball2
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

object{ Ball
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

object{ Ball2
         translate <R,0.00,0>
         rotate <0,Nr* 360/EndNr,0>
       }
#declare Nr = Nr+1;

}

object {
    PBC
    translate <-4,0,0>
}

object {
    APBC
    translate <4,0,0>
}
//------------------------------------------------------------------- end
