# 3D Modeling and Printing Guide
## 1.	Introduction
Welcome to a mini guide on 3D modeling and 3D printing! This guide will walk you through the basics of creating more mechanical-based solutions using 3D printing. 
## 2.	SolidWorks

### 2.1.	SolidWorks Installation
If you already have a version of SolidWorks installed, you can skip this section. However, if you do not, refer to [this document](https://learn.uwaterloo.ca/d2l/le/content/1017258/viewContent/5387160/View).
<!-- (LINK to doc on LEARN page) to install the latest version (2026). -->
### 2.2.	Creating a New Sketch
After the SolidWorks download is complete, click "Part" to start building your 3D model.

<img width="553" height="448" alt="image" src="https://github.com/user-attachments/assets/7312206b-1794-4a7f-9c98-1a6396ab571c" />

To learn how to draw in SolidWorks and create a part, you can refer to this great tutorial. Getting acquainted with the various tools will be beneficial. You can disregard the drawing instruction section of the guide as it is not necessary for the purpose of this workshop.
### 2.3.	Exporting Your Print
Once you are finished with your 3D model, save and export it as an STL (*.stl) file.
 
<img width="856" height="481" alt="image" src="https://github.com/user-attachments/assets/13410804-d9cd-41f7-b5f7-9fd6bf1aba21" />

## 3.	3D Printing
The type of printers being used in this workshop, use a 3D printing process called Fused Deposition Modeling (FDM) printing, in which a thermoplastic filament is melted and extruded through a nozzle to build objects layer by layer. 
### 3.1.	Print Orientation
One important factor that you should consider before you 3D print your part is part orientation (also called build orientation). How you orient your parts in the printer will play a significant role in delivering the final quality you want. For this overview, consider a cylinder with its center axis vertical. 


#### 3.1.1.	Accuracy
The 3D printer would create this part as a stack of concentric circles if you were to print this cylinder vertically. This would result in a finished cylinder with a comparatively smooth outside.  The part will be constructed as a sequence of rectangles (with somewhat varying widths) stacked on top of one another if you were to realign it with its center axis horizontally. Also, the surface of the cylinder that touches the build platform will be flat which may not be ideal depending on the cylinders intended use. 
#### 3.1.2.	Print Time
Because there are fewer layers overall, printing in the horizontal position will take a lot less time than printing in the vertical. The horizontal cylinder will have 100 total layers printed at a layer height of 100 μm, while the vertical cylinder will have 300 layers. For larger parts, this can result in considerable time disparities. Keep in mind the accuracy mentioned above though!
#### 3.1.3.	Strength 
Parts produced by FDM printers are naturally anisotropic, which means that their strength is greater in the XY direction than in the Z direction. It's critical to take into account both the application and the direction of the loads when designing functioning elements. For instance, when placed under tension in the Z direction as opposed to the XY directions, FDM parts are far more likely to delaminate and fracture (with a tensile strength difference of up to 4-5 times).

<img width="578" height="204" alt="image" src="https://github.com/user-attachments/assets/633f75e5-adc4-4dfa-9e5d-29b0bf520e05" />
 
#### 3.1.4.	Surface Finishes
Although this varies from procedure to process, the top or upward-facing surfaces of a 3D-printed component will often have the best surface polish. The extrusion tip smoothes the top surface in FDM, the surface that encounters the print bed is typically glossy, and the surfaces above support structures contain support marks.
### 3.2.	Supports
Generally, whatever auto support option the slicing program offers should be plenty for setting up your 3D print. You should still be aware of the following, though:
- Each layer in FDM printing is created as a collection of heated filament threads that stick to the threads surrounding and beneath it. 
- By printing each thread slightly offset from its preceding layer, a model can be constructed up to 45-degree angles. This allows prints to grow wider than the previous filament layers.
- A feature may sag enough to possibly destroy the print if the overhang is more than 45 degrees. Support structures are necessary at this point.

<img width="672" height="189" alt="image" src="https://github.com/user-attachments/assets/c6804721-73bd-4d6a-a61a-eb4d8da35c7f" />

Imagine you are 3D printing models of the letters Y, H, and T:
- The arms of the letter Y can be readily printed on an FDM printer without the need for support structures.
  - These features are outstretched, but they don’t go beyond 45 degrees.
- It’s a little trickier with the letter H because if the middle bridge is less than 5mm, it can be printed without sagging or support.
  - Support is required if the bridge is more than 5mm.
- The top features that protrude from either side of the model must be supported for the letter T.
  - Without any supports, the material will collapse because there is nothing to print these arms on. 

<img width="511" height="140" alt="image" src="https://github.com/user-attachments/assets/4257e37a-14bd-47ce-a3d0-9e27c1be0613" />

This overhang rule has an exception in some situations. Short distances can be covered by stretching hot material between two print points. Bridging is the term for this technique. Parts can be produced with little sagging and without the need for support material thanks to bridging. To obtain a precise surface quality, support structures are necessary for bridges longer than 5mm.
