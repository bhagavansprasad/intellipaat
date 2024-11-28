# AI

### Rudra Sharma - Onedrive link
```text
OneDrive - https://drive.google.com/drive/folders/1XNdo1eDu1Kd0thn_1uanzzrxQh96Is70?usp=sharing
Instagram - https://www.instagram.com/beardandbinary/
Youtube - www.youtube.com/@beardandbinary
```

####  Relationship between **Input**, **Filter size**, **Stride**, **Pooling**, and **Output image**:
#### 1. **Input (\(I_h \times I_w \times I_d\)):**
   - The **input** is the image or feature map with dimensions:
     \[
     I_h \text{ (height)} \times I_w \text{ (width)} \times I_d \text{ (depth or channels, e.g., RGB = 3)}.
     \]
   - The size of the input determines how many filters and operations are needed to process it.
   - Larger inputs require more computational resources.

#### 2. **Filter Size (\(F_h \times F_w\)):**
   - Defines the spatial size of the kernel applied to the input feature map.
   - Filters with dimensions \(F_h \times F_w \times I_d\) slide across the input depth-wise, producing one channel in the output feature map per filter.

#### 3. **Stride (\(S\)):**
   - Specifies how far the filter moves at each step along the width and height of the input.
   - Larger strides result in fewer overlaps and smaller output dimensions.
   - Smaller strides increase overlaps, preserving more information but making the output dimensions larger.

#### 4. **Pooling (\(P_h \times P_w\)):**
   - Aggregates information from a smaller region of the input feature map (e.g., max pooling or average pooling).
   - The pooling operation has its own window size (\(P_h \times P_w\)) and stride (\(P_s\)) that determine how much the input is downsampled.
   - Pooling reduces spatial resolution, making the output smaller but retaining critical features.

#### 5. **Output Image (\(O_h \times O_w \times O_d\)):**
   - The output dimensions are determined by the **input dimensions**, **filter size**, **stride**, **padding**, and **pooling**.
   - For **convolution** (before pooling):
     \[
     O_h = \left\lfloor \frac{I_h - F_h + 2P_d}{S} \right\rfloor + 1
     \]
     \[
     O_w = \left\lfloor \frac{I_w - F_w + 2P_d}{S} \right\rfloor + 1
     \]
     \[
     O_d = \text{number of filters}.
     \]
   - For **pooling**:
     \[
     O_{pool\_h} = \left\lfloor \frac{O_h - P_h}{P_s} \right\rfloor + 1
     \]m
     \[
     O_{pool\_w} = \left\lfloor \frac{O_w - P_w}{P_s} \right\rfloor + 1
     \]

#### Relationship Summary:
1. **Input** (\(I_h \times I_w \times I_d\)): Determines the starting dimensions of the feature map.
2. **Filter Size (\(F_h \times F_w\))**: Controls the receptive field and feature extraction resolution.
3. **Stride (\(S\))**: Affects how much of the input is skipped per step, influencing output size.
4. **Pooling (\(P_h \times P_w\), \(P_s\))**: Reduces spatial dimensions further by summarizing feature maps.
5. **Output Image (\(O_h \times O_w \times O_d\))**: The result of convolution and pooling, its size is affected by \(I_h, I_w, F_h, F_w, S, P_h, P_w, P_s, P_d\). 

In essence:
- Larger **inputs** lead to larger **outputs** unless **filters**, **strides**, and **pooling** are used to reduce dimensions.
- Larger **filters** and **strides** decrease the spatial resolution of the output more aggressively.
- **Pooling** further shrinks dimensions while retaining key features.