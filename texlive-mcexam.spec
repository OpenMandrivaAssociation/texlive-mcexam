%global tl_name mcexam
%global tl_revision 60481

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Create randomized Multiple Choice questions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mcexam
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcexam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcexam.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package automatically randomly permutes the order of
questions as well as the answer options in different versions of a
multiple choice exam/test. Next to the exam versions themselves, the
package also allows printing a concept version of the exam, a key table
with the correct answers or points, and a document with solutions and
explanations per exam version. The package also allows writing an R code
which processes the results of the exam and calculates the grades. The
following other LaTeX packages are required: enumitem, environ,
etoolbox, longtable, newfile, pgffor (from the PGF/TikZ bundle),
xkeyval, and xstring.

