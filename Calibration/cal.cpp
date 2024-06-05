void graph(const char *path, TGraphErrors *g1, const char *name){
    g1->Fit("pol1");
    TString s(name);
    TString label(";ticks;ns");
    TString title(s + label);
    g1->SetTitle(title);
    g1->SetMarkerStyle(8);
    g1->SetMarkerColor(kBlack);
    g1->SetMarkerSize(.4);
    g1->SetLineStyle(1);
    g1->SetLineWidth(1.);
    TCanvas *c = new TCanvas(path,name);
    g1->Draw();
    TString pathtopdf("pdf/" + s +".pdf");
    c->SaveAs(pathtopdf);   
    TF1 *par = (TF1*)g1->GetListOfFunctions()->FindObject("pol1");
    double resP0 = par->GetParameter(0);
    double resP1 = par->GetParameter(1);
    TString nameresq("calres/" + s +"q.txt");
    TString nameresm("calres/" + s +"m.txt");
    ofstream PMq;
    PMq.open (nameresq);
    PMq << resP0;
    PMq.close();

    ofstream PMm;
    PMm.open (nameresm);
    PMm << resP1;
    PMm.close();

}

void cal(const char *path1="results/PMT1.txt",const char *path2="results/PMT2.txt",const char *path3="results/PMT3.txt")
{
    gStyle->SetOptFit(0110);
    gStyle->SetStatX(0.9);
    gStyle->SetStatY(0.9);
    gStyle->SetStatW(0.1);
    gStyle->SetStatH(0.05);

    TGraphErrors* g1 = new TGraphErrors(path1, "%lg %lg %lg %lg", ",");
    TGraphErrors* g2 = new TGraphErrors(path2, "%lg %lg %lg %lg", ",");
    TGraphErrors* g3 = new TGraphErrors(path3, "%lg %lg %lg %lg", ",");

    graph("PMT1",g1,"PMT1");
    graph("PMT2",g2,"PMT2");
    graph("PMT3",g3,"PMT3");

}