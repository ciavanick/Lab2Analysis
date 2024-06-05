void Analysis(TString path = "Filtering/cleanandconv/P1.txt", TString name = "PMT1") {
    gStyle->SetOptFit(111);
    gStyle->SetOptStat(10);
    
    TTree* t = new TTree("t", "Tree");
    t->ReadFile(path, "tP/D");
    
    TH1F* h = new TH1F("h", "times in P1", 80, 0., 16500.);
    t->Draw("tP >> h");

    h->SetTitle("Decay time in P;Time (ns);Counts");
    h->SetFillColor(kCyan - 10);
    
    Double_t R = 1.21;

    TF1* f_exp = new TF1("f_exp", "[0] * (e^(-x/[1]) *(1 + (1/1.21) * e^(-x/[2]))) +[3]", 0, 16000);
    
    f_exp->SetParNames("N_{0}", "#tau_{0}", "#tau_{#mu^{-}}", "b");
    f_exp->SetParameters(1000, 2200 ,200, 10);
    
    TFitResultPtr r = h->Fit("f_exp", "HES", "", 200, 16000); //hessian fit
    //h->Fit("f_exp", "HES", "", 200, 16000); //kick root in the ass to work

    TMatrixD cor = r->GetCorrelationMatrix();
    cor.Print();

	// DRAW the exp FUNCTION and background
    
	TF1* f0 = new TF1("f0", "[0]*e^(-x/[1])", 0, 16000);
	f0->SetParameters(f_exp->GetParameter(0), f_exp->GetParameter(1));
	f0->SetLineColor(kBlack);

    TF1* f1 = new TF1("f1", "[0]", 0, 16000);
	f1->SetParameters(f_exp->GetParameter(3));
	f1->SetLineColor(kGreen + 1);

    TLegend* leg = new TLegend(0.55,0.4,0.99,0.615);
    leg->AddEntry(h, "Experimental data");
    leg->AddEntry(f_exp, "Fit:N_{0}e^{-t/#tau_{0}}(1+1/R e^{-t/#tau_{#mu^{-}}})+b");
    leg->AddEntry(f0, "Free muon: N_{0}e^{-t/#tau_{0}}");
    leg->AddEntry(f1, "Background: b");
    
    TCanvas* c = new TCanvas("c", "c");
    c->cd();

    h->Draw();
    f_exp->Draw("Same");
    f0->Draw("Same");
    f1->Draw("Same");
    leg->Draw("Same");
    TString outpath("Results/" + name + ".pdf");
    c->SaveAs(outpath);

    TCanvas* c2 = new TCanvas("c2", "c2");
    c2->SetLogy();
    h->Draw();
    f_exp->Draw("Same");
    f0->Draw("Same");
    f1->Draw("Same");
    leg->Draw("Same");
    TString outpathlog("Results/" + name + "log.pdf");
    c2->SaveAs(outpathlog);

    
    
}