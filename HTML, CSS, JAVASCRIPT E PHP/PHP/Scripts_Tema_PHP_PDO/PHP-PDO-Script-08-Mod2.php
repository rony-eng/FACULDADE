PDOStatement implements Traversable {
    /* Propriedades */
    readonly string $queryString;
    
    /* Métodos */
    public bindColumn ( mixed $column , mixed &$param [, int $type [, int $maxlen [, 
    mixed $driverdata ]]] ) : bool
    public bindParam ( mixed $parameter , mixed &$variable [, int $data_type = 
    PDO::PARAM_STR [, int $length [, mixed $driver_options ]]] ) : bool
    public bindValue ( mixed $parameter , mixed $value [, int $data_type = 
    PDO::PARAM_STR ] ) : bool
    public closeCursor ( void ) : bool
    public columnCount ( void ) : int
    public debugDumpParams ( void ) : void
    public errorCode ( void ) : string
    public errorInfo ( void ) : array
    public execute ([ array $input_parameters = NULL ] ) : bool
    public fetch ([ int $fetch_style [, int $cursor_orientation = 
    PDO::FETCH_ORI_NEXT [, int $cursor_offset = 0 ]]] ) : mixed
    public fetchAll ([ int $fetch_style [, mixed $fetch_argument [, array $ctor_args 
    = array() ]]] ) : array
    public fetchColumn ([ int $column_number = 0 ] ) : mixed
    public fetchObject ([ string $class_name = "stdClass" [, array $ctor_args ]] ) : 
    mixed
    public getAttribute ( int $attribute ) : mixed
    public getColumnMeta ( int $column ) : array
    public nextRowset ( void ) : bool
    public rowCount ( void ) : int
    public setAttribute ( int $attribute , mixed $value ) : bool
    public setFetchMode ( int $mode ) : bool
}