import streamlit as st
# from pyscf import gto, dft
# import numpy as np

# Set page config
st.set_page_config(page_title='CrysX-DEMO: Density Functional Theory', layout='wide', page_icon="🧊",
menu_items={
         'About': "# This is an online demo of DFT and related methods in action. It lets you perform your own calculations for small systems with less than 50 basis functions."
     })

# Sidebar stuff
st.sidebar.write('# About')
st.sidebar.write('### Made By [Manas Sharma](https://manas.bragitoff.com)')
st.sidebar.write('### *Powered by*')
st.sidebar.write('* [PySCF](https://pyscf.org/) for Molecular Integrals and DFT Calculations')
st.sidebar.write('* [Py3Dmol](https://3dmol.csb.pitt.edu/) for Chemical System Visualizations')
st.sidebar.write('* [Streamlit](https://streamlit.io/) for making of the Web App')
st.sidebar.write('## Brought to you by [CrysX](https://www.bragitoff.com/crysx/)')
# st.sidebar.write('## Cite us:')
# st.sidebar.write('[Sharma, M. & Mishra, D. (2019). J. Appl. Cryst. 52, 1449-1454.](http://scripts.iucr.org/cgi-bin/paper?S1600576719013682)')


# Main app
st.write('# CrysX-DEMO: Density Functional Theory')
st.write('#### This is an online interactive demo of density functional theory (DFT) and related methods.')
st.write(' It lets you perform your own calculations for small systems with less than 50 basis functions.')


intro_text = '''
The purpose of this interactive web application is to allow beginners to get a hands-on experience while learning some of the key concepts of DFT and related methods. I hope that this would serve as a reasonably fast method of making you familiar with DFT, Hartree-Fock, Time Dependent DFT (TDDFT), Geometry Optimization, etc.
'''

st.write(intro_text)
st.image('dft_pic.png')
st.write('### Introduction')
st.write('DFT is a computational tool based on quantum mechanics and is used to investigate the electronic structure of many-body systems like atoms, molecules and solids. Traditional electronic structure methods attempt to find approximate solutions to the Schrodinger equation of N interacting electrons moving in an external, electrostatic potential (typically the Coulomb potential generated by the atomic nuclei)')

st.write('A different approach is taken in density functional theory where, instead of the manybody wave-function, the one-body density is used as fundamental variable. Since the density n(r) is a function of only three spatial coordinates (rather than the 3N coordinates of the wave-function), density functional theory is computationally feasible even for large systems.')






st.write('### The Hohenberg−Kohn Theorems')
st.write('1. The ground state electron density n(r) of a system of interacting electrons uniquely determines the external potential v(r) in which the electrons move and thus the Hamiltonian and all physical properties of the system.')
st.write('2. The second part of the Hohenberg–Kohn theorem provides a variational principle for the electron density. For any density ρ, the energy functional Ev[ρ] will lead to an energy that is larger or equal to the ground-state energy, i.e.,')
st.latex(r'E_v[\rho] \geq E_0 \quad \forall \rho')
st.write('Therefore, the ground-state energy and the ground-state density ρ0 can be calculated by minimizing the total-energy functional Ev[ρ], i.e.,')
st.latex(r'E_0=\min _\rho E_v[\rho]')
st.write('where the search space includes all densities that correspond to an antisymmetric N-electron wave function. This search space is much smaller than that of all antisymmetric wave functions, thus simplifying the initial problem considerably.')






st.write('### Kohn-Sham Equations')
st.write('The Kohn–Sham equation is the non-interacting Schrödinger-like equation of a fictitious system (the "Kohn–Sham system") of non-interacting electrons that generate the same density as any given system of interacting particles.')
st.write('The Kohn–Sham equation is defined by a local effective (fictitious) external potential in which the non-interacting particles move, typically denoted as vs(r) or veff(r), called the Kohn–Sham potential. The Kohn–Sham wavefunction is a single Slater determinant constructed from a set of orbitals that are the lowest-energy solutions to')
st.latex(r'\left(-\frac{\hbar^2}{2 m} \nabla^2+v_{\text {eff }}(\mathbf{r})\right) \varphi_i(\mathbf{r})=\varepsilon_i \varphi_i(\mathbf{r})')
st.write('Here εi is the orbital energy of the corresponding Kohn–Sham orbital ϕi, and the density for an N-particle system is')
st.latex(r'\rho(\mathbf{r})=\sum_i^N\left|\varphi_i(\mathbf{r})\right|^2')
st.write('The Kohn–Sham equations are found by varying the total energy expression with respect to a set of orbitals, subject to constraints on those orbitals, to yield the Kohn–Sham potential as')
st.latex(r'v_{\mathrm{eff}}(\mathbf{r})=v_{\mathrm{nuc}}(\mathbf{r})+ \int \frac{\rho\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} d \mathbf{r}^{\prime}+\frac{\delta E_{\mathrm{xc}}\lfloor\rho\rfloor}{\delta \rho(\mathbf{r})}')

st.write('where the first term is the potential due to the nuclei, the second term is the Hartree (electronic Coulomb potential) and the last term is the exchange-correlation functional.')
st.write('To solve the KS equations in practice, the KS orbitals are expanded in basis function,')
st.latex(r'\varphi_i(\boldsymbol{r})=\sum_{j=1}^M C_{i j} \chi_j(\boldsymbol{r})')
st.write('where $\chi_i$')


st.write('### References')
st.write('[https://www-old.mpi-halle.mpg.de/mpi/publi/br/gross_persoenlich/KMG05.pdf](https://www-old.mpi-halle.mpg.de/mpi/publi/br/gross_persoenlich/KMG05.pdf)')
st.write('[https://pubs.acs.org/doi/full/10.1021/cr990029p](https://pubs.acs.org/doi/full/10.1021/cr990029p)')
st.write('[https://en.wikipedia.org/wiki/Kohn%E2%80%93Sham_equations](https://en.wikipedia.org/wiki/Kohn%E2%80%93Sham_equations)')
st.write('[https://www.southampton.ac.uk/assets/centresresearch/documents/compchem/DFT_L6.pdf](https://www.southampton.ac.uk/assets/centresresearch/documents/compchem/DFT_L6.pdf)')
st.write('[https://www.tcm.phy.cam.ac.uk/~pdh1001/thesis/node17.html](https://www.tcm.phy.cam.ac.uk/~pdh1001/thesis/node17.html)')
