/*-----------------------------------------------------------------------------
	cord name = [ ptv4t.c ]

#	B

	2007/10/29 Yuji TASAKA in Hokkaido UNIV(Lab. for Flow Contorl)
	2007/11/29 Tetsushi Kanda  in Hokkaido UNIV(Lab. for Flow Contorl)
-----------------------------------------------------------------------------*/

#include "hulfc.h"


typedef struct {
	double x; double y;
} Vect;

typedef struct {
	double gap; double angle;
} Gap;

typedef struct {
	int p1;
	int p2;
	float err;
	int flg;
} tPi;

/*---------------------------- ProtoType Function ---------------------------*/
int Read_NumP(char *fname);			// for reading the numner of particle
int Read_PP(char *fname, Vect *pp);	// for reading particle position
Vect Rot(Vect dx, double angle);    // for rotating difference vector
Gap Calc_gap(Vect dx1, Vect dx2);	// for calculating assessment parameters

/*------------------------------- Main Function -----------------------------*/
int	main(int argc, char **argv)
{
	FILE *fp;

	char ch, *tmp;
	char pp_FILE[4][64];					// file name
	char S_FILE[64] = "displacement.csv";	// file name

	Vect *pp[4];							// particle positions at each image
	tPi  *pp12;                             // Information of tracked particle

	double xp, yp, dxp, dyp;                // Particle position & particle displacement
	Vect   dx[3];    						// Particle displacement for image by image

	double distance;                        // distance between particles
	Gap    dst[2];                          // gap:   gap between particle position and estimated particle position
											// angle: angle between particle position and estimated particle position

	float s1 = 20.0, s2 = 14.0;             // 1st and 2nd search range
	float et = 13.0;                        // criterion on angle [13 deg]
	float cf, cfc;                          // criterion factor

	int nump[4];                            // The numner of particle in each file
	int npa = -1;                           // The numnber of available particle

	int flag;                               // flag for the particle tracking
	int ntsp = 0;                           // the number for tracking the same particle

	int count;
	int ii, jj, kk, ll;

/*--------------------- Parameter control -------------------------*/

	if (argc < 5){
		puts("ptv4t [Image1] [Image2] [Image3] [Image4] -o [OutpFile] ");
		puts("      -1 [SearchRange1] -2 [SearchRange2] -a [SearchAngle]");
		puts("  [Image1-4] : Input file name at each time");
		printf("  -o     : Output filename (default %s)\n", S_FILE);
		printf("  -1     : Radius of the 1st search area (default %6.2f [pixel])\n", s1);
		printf("  -2     : Radius of the 2nd search area (default %6.2f [pixel])\n", s2);
		printf("  -a     : Criterion for angle (default %5.2f [deg])\n", et);
		exit(0);
    }

	if(argc>5){
		count=4;
		do{
			count++;
			tmp=argv[count];
			if(*argv[count]=='-'){
				ch=*(++tmp);
				switch(ch){
					case 'o' :
						count++;
						/* SetFileOutp=TRUE; */
						strcpy(S_FILE,argv[count]);
						printf(" read parameter -o %s\n", S_FILE);
					break;
				    case '1' :
						count++;
						s1 = (float)atof(argv[count]);
						printf(" read parameter -1 %6.2f\n", s1);
					break;
				    case '2' :
						count++;
						s2 = atof(argv[count]);
						printf(" read parameter -2 %6.2f\n", s2);
					break;
					case 'a' :
						count++;
						et = atof(argv[count]);
						printf(" read parameter -a %5.2f\n", et);
					break;
				    default :
					printf("error on command line(1)\n");
					exit(0);
				}
			}
			else{
				printf("error on command line(2)\n");
				exit(0);
			}
		}while(count<argc-1);
	}
	puts(" ");


/*--------------------Reading particle position at each time ----------------*/

	for (ii=0; ii<4; ii++){
		strcpy(pp_FILE[ii], argv[ii+1]);
//		printf(" Particle position file %d: %s\n", ii+1, pp_FILE[ii]);
		nump[ii] = Read_NumP(pp_FILE[ii]);
	}

    //memory allocation
	for (ii=0; ii<4; ii++) pp[ii] = (Vect *)calloc( nump[ii], sizeof(Vect));

	pp12 = (tPi (*))calloc( nump[0], sizeof(tPi));

	for (ii=0; ii<4; ii++) Read_PP(pp_FILE[ii], pp[ii]);

/*---------------------------- 4 times tracking -----------------------------*/

	for (ii=0; ii<nump[0]; ii++){                  // 1st image
		flag = 0;                                  // clearing the flag for the particle tracking
//		printf("%d /%d\n", ii+1, nump[0]);
		cf = 5000.0;                               // arbitrary large number
		for(jj=0; jj<nump[1]; jj++){               // 2nd image
			dx[0].x = pp[1][jj].x - pp[0][ii].x;
			dx[0].y = pp[1][jj].y - pp[0][ii].y;
			distance = sqrt(dx[0].x * dx[0].x + dx[0].y * dx[0].y);
			if (distance <= s1){

				for (kk=0; kk<nump[2]; kk++){                  // 3rd image
					dx[1].x = pp[2][kk].x - pp[1][jj].x;
					dx[1].y = pp[2][kk].y - pp[1][jj].y;
					dst[0] = Calc_gap(dx[0], dx[1]);
					dx[1] = Rot(dx[1], dst[0].angle);  //rotation of difference vector
					if ((dst[0].gap <= s2)&&(fabs(dst[0].angle*180.0/PI) <= et)){

						for (ll=0; ll<nump[3]; ll++){          // 4th image
							dx[2].x = pp[3][ll].x - pp[2][kk].x;
							dx[2].y = pp[3][ll].y - pp[2][kk].y;
							dst[1] = Calc_gap(dx[1], dx[2]);
							cfc = dst[0].gap*dst[0].gap + dst[1].gap*dst[1].gap;

							if ((dst[1].gap <= s2)&&(fabs(dst[1].angle*180.0/PI) <= et)&&(cfc < cf)){
								cf = cfc;
								if (flag == 0) npa++;
//							    printf("%d %d\n", ii+1, npa);
								pp12[npa].p1 = ii;
								pp12[npa].p2 = jj; //position of the tracked particle
								pp12[npa].err = cf;
								pp12[npa].flg = 0;
								flag = 1;
							}
						}
					}
				}
			}
		}
    }
	npa++;
	printf( "\n The number of available particle: %d\n", npa);

/*-------------------------- post processing ------------------------ */

	for (ii=0; ii<npa; ii++){
		if (pp12[ii].flg == 0){
			for (jj=ii+1; jj<npa; jj++){
				if (pp12[ii].p2 == pp12[jj].p2){   //If different particles track the same particle.....
					                               //giving an error flag to particle which has larger error.
					if (pp12[ii].err > pp12[jj].err){
						pp12[ii].flg = 1;
						ntsp++;
						break;
					}
					else pp12[jj].flg = 1;
					ntsp++;
				}
			}
		}
	}
	printf(" The number for tracking the same particle: %d\n", ntsp);
	printf(" The number of remaining particle by post processing: %d\n", npa - ntsp);

/*---------------------------- displacement ------------------------- */

	fp = fopen(S_FILE, "w");

	//header for Graph R format
	fprintf(fp, "data format,5\n");

	fprintf(fp, "%d\n", npa - ntsp);
	fprintf(fp, "x,y,,dx,dy,,\n");

	for (ii=0; ii<npa; ii++){
		if (pp12[ii].flg == 0){
			xp =  pp[0][pp12[ii].p1].x; yp = pp[0][pp12[ii].p1].y;
			dxp = pp[1][pp12[ii].p2].x - pp[0][pp12[ii].p1].x;
			dyp = pp[1][pp12[ii].p2].y - pp[0][pp12[ii].p1].y;
			fprintf(fp, "%lf,%lf,,%lf,%lf,\n", xp, yp, dxp, dyp);
		}
	}

	fclose(fp);

	return 0;
}

/*-------------------------------Reading the number of particle------------------*/
int Read_NumP(char *fname)
{

	FILE *fp;
	int num;


	OpenFile(fp, fname, "r");
	fscanf(fp, "%d\n", &num);
//	printf("%s %d\n", fname, num);

	fclose(fp);

	return num;
}

/*----------------------------File reader -----------------------------------*/
int Read_PP(char *fname, Vect *pp)
{

	FILE *fp;
	char tmp[5000];
	int ii;
	int num;
	int count;

	OpenFile(fp, fname, "r");
	fgets(tmp, 5000, fp);
	num = atoi(strtok(tmp, ","));
	fgets(tmp, 5000, fp);
	printf(" The number of particle [%s]: %d\n", fname, num);

	for (ii=0; ii<num; ii++){
		fgets(tmp, 5000, fp);
		count = atoi(strtok(tmp, ","));
		pp[ii].x = atof(strtok(NULL, ","));
		pp[ii].y = atof(strtok(NULL, ","));
//		printf("%f\n", pp[ii].x);
	}

	fclose(fp);

	return 0;
}

/* ------------------------- Rotation of difference vector ---------------- */

Vect Rot(Vect dx, double angle)
{
	Vect tmp;

	tmp.x = dx.x * cos(angle) - dx.y * sin(angle);
	tmp.y = dx.x * sin(angle) + dx.y * cos(angle);

	return tmp;
}


/*-------------------- Calculator of assessment parameters -----------------*/
Gap Calc_gap(Vect dx1, Vect dx2)
{
	Vect gx;
	Gap dst;
	double inner_product, outer_product;

	gx.x = dx2.x - dx1.x;
	gx.y = dx2.y - dx1.y;
	dst.gap = sqrt(gx.x * gx.x + gx.y * gx.y);
	inner_product = dx1.x * dx2.x + dx1.y * dx2.y;
	outer_product = dx1.x * dx2.y - dx1.y * dx2.x;

	inner_product /= (sqrt(dx1.x * dx1.x + dx1.y * dx1.y)
		            * sqrt(dx2.x * dx2.x + dx2.y * dx2.y));
	if (inner_product > 1.0) inner_product /= fabs(inner_product);
	dst.angle = acos(inner_product);           //The angle is given in Radian
	if (outer_product < 0) dst.angle *= -1.0;

	return dst;
}