Name:		texlive-mcexam
Version:	60481
Release:	2
Summary:	Create randomized Multiple Choice questions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mcexam
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcexam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcexam.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package automatically randomly permutes the order of
questions as well as the answer options in different versions
of a multiple choice exam/test. Next to the exam versions
themselves, the package also allows printing a concept version
of the exam, a key table with the correct answers or points,
and a document with solutions and explanations per exam
version. The package also allows writing an R code which
processes the results of the exam and calculates the grades.
The following other LaTeX packages are required: enumitem,
environ, etoolbox, longtable, newfile, pgffor (from the
PGF/TikZ bundle), xkeyval, and xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mcexam
%doc %{_texmfdistdir}/doc/latex/mcexam

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
