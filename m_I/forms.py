from django import forms

class Mean(forms.Form):
    #Radius_mean = forms.FloatField()
    Texture_mean = forms.FloatField(label_suffix='(9-40)')
    #Perimeter_mean=forms.FloatField()
    Area_mean =forms.FloatField(label_suffix='(143-2501)')
    Smoothness_mean  = forms.FloatField(label_suffix='(0-0.1634)')
    #Compactness_mean = forms.FloatField()
    Concavity_mean = forms.FloatField(label_suffix='(0-0.4268)')
    #Concave_points_mean  = forms.FloatField()
    Symmetry_mean    = forms.FloatField(label_suffix='(0-0.304)')
    Fractal_dimension_mean = forms.FloatField(label_suffix='(0-0.09744)')
class SymanticError(forms.Form):
    #Radius_se = forms.FloatField()
    Texture_se= forms.FloatField(label_suffix='(0.4-4.885)')
    #Perimeter_se=forms.FloatField()
    Area_se =forms.FloatField(label_suffix='(6.80200-542.2)')
    Smoothness_se = forms.FloatField(label_suffix='(0.001713-0.03113)')
    #Compactness_se = forms.FloatField()
    Concavity_se = forms.FloatField(label_suffix='(0-0.396)')
    #Concave_points_se  = forms.FloatField()
    Symmetry_se   = forms.FloatField(label_suffix='(0.007882-0.07895)')
    fractal_dimension_se = forms.FloatField(label_suffix='(0-0.029841)')
class Worst(forms.Form):
    #Radius_worst = forms.FloatField()
    #Texture_worst = forms.FloatField()
    #Perimeter_worst=forms.FloatField()
    #Area_worst=forms.FloatField()
    Smoothness_worst  = forms.FloatField(label_suffix='(0.-0.2226)')
    #Compactness_worst = forms.FloatField()
    Concavity_worst = forms.FloatField(label_suffix='(0-1.252)')
    #Concave_points_worst  = forms.FloatField()
    Symmetry_worst    = forms.FloatField(label_suffix='(0.1565-0.6638)')
    Fractal_dimension_worst = forms.FloatField(label_suffix='(0.05504-0.2075)')




