from django import forms
from .models import AtaqueVocal, Loudness, Modulacao, Pitch, Qualidadeemis, Ressonancia, TipoVoz, comunicoral_comunicoral, paciente_paciente
from .models import profissionalenc_profissionalenc
from django import forms

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente_paciente
        fields = ('RG','CPF','nome', 'DataNascimento', 'sexo', 'Profissional_id')

class profissionalForm(forms.ModelForm):
    class Meta:
        model = profissionalenc_profissionalenc
        fields = ('nome','status')
        
class ComunicOralForm(forms.ModelForm):
    class Meta:
        model = comunicoral_comunicoral
        fields = '__all__'        
        
class TipoVozForm(forms.ModelForm):
    class Meta:
        model = TipoVoz
        fields = '__all__'
        
class RessonanciaForm(forms.ModelForm):
    class Meta:
        model = Ressonancia
        fields = '__all__'                
        
class AtaqueVocalForm(forms.ModelForm):
    class Meta:
        model = AtaqueVocal
        fields = '__all__'        
        
class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = '__all__'

class LoudnessForm(forms.ModelForm):
    class Meta:
        model = Loudness
        fields = '__all__'
        
class ModulacaoForm(forms.ModelForm):
    class Meta:
        model = Modulacao
        fields = '__all__'                
        
class QualidadeemissForm(forms.ModelForm):
    class Meta:
        model = Qualidadeemis
        fields = '__all__'        