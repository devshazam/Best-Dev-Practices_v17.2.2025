FLEX:

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.flex-item{

}



GRID:

.grid-container{
    display: grid;
    grid-template-columns: repeat(2, 1fr); // 2 is a number of potential columns
    row-gap: 10px;
    column-gap: 10px:
}
.grid-item{
     grid-column: span 1; // 1 is a width of column
}